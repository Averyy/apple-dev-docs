# Updating and deleting keychain items

**Framework**: Security

Modify items in the keychain when the user’s data changes.

#### Overview

If, outside the flow of your app, the user changes a password that your app stores in the keychain, you may discover the change only when authentication with that password fails. In response, your app prompts the user for the new credentials and updates the keychain to reflect the change.

During this process, if you try to store the new set of credentials using a call to the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function, you may find that the operation fails. With primary attributes the same as an existing item, the new item can’t coexist with the old one in the keychain. Even if a primary attribute (such as the user name) does change and the add operation succeeds, you end up cluttering the keychain with old, abandoned items. These may be hard to distinguish from the one you actually need. To avoid these problems, update the existing item instead.

##### Prepare a Search Query and New Attributes

To update keychain items, you first need to find them. So an update begins with an implicit search just like the one explicitly performed by the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function. To control this implicit search, just as for the explicit search, you create a query dictionary:

```swift
let query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                            kSecAttrServer as String: server]
```

This particular query indicates a search for an Internet password associated with your `server`. Be aware that this matches (and also updates) any such passwords that you’ve stored. If you’re using the keychain for other storage, you may need to further qualify this search to ensure that you only affect the item of interest. Because you’re not retrieving the data, there’s no need to specify a return type.

In addition to supplying the search query, you supply a second dictionary to describe your desired changes. You can provide new item data, such as for changing a stored password, using the [`kSecValueData`](ksecvaluedata.md) key. And you can change an item’s attributes—for example, updating the account by using the [`kSecAttrAccount`](ksecattraccount.md) key:

```swift
let account = credentials.username
let password = credentials.password.data(using: String.Encoding.utf8)!
let attributes: [String: Any] = [kSecAttrAccount as String: account,
                                 kSecValueData as String: password]
```

You provide the user name and password given by the user, passed through a `C``redentials` instance. It’s OK if the user name happens to be the same as the existing value and only the password data changes.

##### Execute an Update

Using the search query and the new attributes, call the [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) function:

```swift
let status = SecItemUpdate(query as CFDictionary, attributes as CFDictionary)
guard status != errSecItemNotFound else { throw KeychainError.noPassword }
guard status == errSecSuccess else { throw KeychainError.unhandledError(status: status) }
```

Make sure you test the status returned by the call and handle any failure. When successful, the call modifies all matching items according to the attributes you provide.

##### Delete Items That You No Longer Need

If the user decides to log out of your server from within your app, you’ll want to remove the password item from the keychain as part of that process. Deleting an item is very much like updating it, except that it only requires the query dictionary. You can use the same query defined earlier, this time with a call to the [`SecItemDelete(_:)`](secitemdelete(_:).md) function:

```swift
let status = SecItemDelete(query as CFDictionary)
guard status == errSecSuccess || status == errSecItemNotFound else { throw KeychainError.unhandledError(status: status) }
```

By default, keychain services deletes all keychain items that match the search parameters. If you want to delete a specific item that you already have a reference or persistent reference to, add that to the search dictionary as the value for the [`kSecMatchItemList`](ksecmatchitemlist.md) key. In this way, you limit the deletion to only the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/updating-and-deleting-keychain-items)*