# Searching for keychain items

**Framework**: Security

Find keychain items based on search criteria that you specify.

#### Overview

You find keychain items using a query dictionary that tells the keychain services API what item attributes to look for and what to return when a match is found. The query dictionary also lets you specify additional parameters to refine the search. For example, you can control case sensitivity when matching string attributes or limit the number of matches.

As an example of conducting a search, consider the password item stored in [`Adding a password to the keychain`](adding-a-password-to-the-keychain.md). After providing credentials (that your app stores) for a network service, the user works with your app for a while and then eventually moves on to something else. When the user returns, your app may need to reauthenticate with the server in order to continue working. This time the app loads the password from the keychain instead of bothering the user with a login view.

##### Create a Search Query

Begin the search by constructing a query dictionary:

```swift
let query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                            kSecAttrServer as String: server,
                            kSecMatchLimit as String: kSecMatchLimitOne,
                            kSecReturnAttributes as String: true,
                            kSecReturnData as String: true]
```

This query searches for Internet password items that have `server` attributes matching the `server` attribute you previously used when adding the password item. The query also limits the results to a single value (which is actually the default behavior) using the [`kSecMatchLimit`](ksecmatchlimit.md) search parameter. You receive only the first match found in the keychain, if any.

Finally, the query requests from the password item both its attributes and its data. You need both, because the [`kSecAttrAccount`](ksecattraccount.md) attribute contains the user name and the item’s data holds the password itself.

> **Note**:  By default, your app can freely retrieve its own keychain items but not those of other apps. However, keychain services does provide mechanisms for broadening or narrowing that accessibility, for example, using the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) attribute.

##### Initiate the Search

After you’ve created the query dictionary, you initiate the search with a call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function:

```swift
var item: CFTypeRef?
let status = SecItemCopyMatching(query as CFDictionary, &item)
guard status != errSecItemNotFound else { throw KeychainError.noPassword }
guard status == errSecSuccess else { throw KeychainError.unhandledError(status: status) }
```

As you do with many Security framework functions, you first test the returned status value. Among other things, an error might occur if no matching item is found — for example, because you didn’t previously store a password for the given `server`. If an error occurs, you receive the [`errSecItemNotFound`](errsecitemnotfound.md) result, which you might want to treat differently from a general error. In fact, detecting this error is one way to recognize that you’re making your first pass through your app’s login flow, before you’ve stored anything.

When the search succeeds, the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function provides a result through its `item` parameter. The type of the returned item depends on the nature of the query, as described in [`Item return result keys`](item-return-result-keys.md).

##### Extract the Result

Because in your search you requested multiple return types and allowed only a single result, you should expect the result to be a dictionary. You recover the user name from the attribute value associated with the [`kSecAttrAccount`](ksecattraccount.md) key. Meanwhile, you use the [`kSecValueData`](ksecvaluedata.md) key to extract the password data, which you then convert to a string:

```swift
guard let existingItem = item as? [String : Any],
    let passwordData = existingItem[kSecValueData as String] as? Data,
    let password = String(data: passwordData, encoding: String.Encoding.utf8),
    let account = existingItem[kSecAttrAccount as String] as? String
else {
    throw KeychainError.unexpectedPasswordData
}
let credentials = Credentials(username: account, password: password)
```

If when conducting the search you instead set the value associated with the [`kSecMatchLimit`](ksecmatchlimit.md) key to an integer number greater than 1, the returned item is an array whose entry count is limited to the value you set. Each entry in this array is formatted like the bare dictionary you obtain when limiting the matches to one. If you specify [`kSecMatchLimitAll`](ksecmatchlimitall.md) for the [`kSecMatchLimit`](ksecmatchlimit.md) key, the array size is limited only by the number of matches found in the keychain.

> **Note**:  You can’t combine the [`kSecReturnData`](ksecreturndata.md) and [`kSecMatchLimitAll`](ksecmatchlimitall.md) options when copying password items, because copying each password item could require additional authentication. Instead, request a reference or persistent reference to the items, then request the data for only the specific passwords that you actually require.

When you do get an array of results, you may need to iterate through the array for a single item of interest. You might do this by examining some other item attribute, such as the account, the creation date, or a label. On the other hand, if you know about a distinguishing characteristic ahead of time, it’s typically more efficient to narrow your initial keychain search query with the corresponding attributes.

Whether or not you need to handle multiple matches at all depends on how your app uses the keychain. If you allow the user to select among different identities at runtime, you might want to store multiple passwords for a single server and then let the user select among the search results using the stored account as a selection key. Other times, you might decide to filter your search down to a single result without involving the user. If you take this approach, make sure that you don’t create similar items in the keychain—test for and then delete or modify existing items instead. See [`Updating and deleting keychain items`](updating-and-deleting-keychain-items.md) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/searching-for-keychain-items)*