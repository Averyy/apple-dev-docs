# Adding a password to the keychain

**Framework**: Security

Add network credentials to the keychain on behalf of the user.

#### Overview

Use keychain services to enable simple, secure storage for users’ passwords. In this way you avoid repeatedly asking the user for a password, and you don’t have to implement your own encryption, which can be error prone.

##### Get Set Up

To get started, define a structure to hold the credentials as they move around your app in memory:

```swift
struct Credentials {
    var username: String
    var password: String
}
```

Next, define an error enumeration that you can use to communicate keychain access outcomes:

```swift
enum KeychainError: Error {
    case noPassword
    case unexpectedPasswordData
    case unhandledError(status: OSStatus)
}
```

Then, identify the server that your app is working with:

```swift
static let server = "www.example.com"
```

##### Create an Add Query

Using an instance of the credentials structure and the server constant, you can create an add query:

```swift
let account = credentials.username
let password = credentials.password.data(using: String.Encoding.utf8)!
var query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                            kSecAttrAccount as String: account,
                            kSecAttrServer as String: server,
                            kSecValueData as String: password]
```

The query dictionary’s first key-value pair indicates that the item is an Internet password, from which keychain services infers that the data is secret and requires encryption. This also ensures that the item has attributes that distinguish it from other Internet passwords, such as the server and account to which it applies. Indeed, the next two key-value pairs in the query provide this information, attaching the user name acquired from the user as the account, along with a domain name appropriate to this password as the server.

> **Note**:  Keychain services also offers the related [`kSecClassGenericPassword`](ksecclassgenericpassword.md) item class. Generic passwords are similar in most respects to Internet passwords, but they lack certain attributes specific to remote access (for example, they don’t have a [`kSecAttrServer`](ksecattrserver.md) attribute). When you don’t need these extra attributes, use a generic password instead.

 Keychain services also offers the related [`kSecClassGenericPassword`](ksecclassgenericpassword.md) item class. Generic passwords are similar in most respects to Internet passwords, but they lack certain attributes specific to remote access (for example, they don’t have a [`kSecAttrServer`](ksecattrserver.md) attribute). When you don’t need these extra attributes, use a generic password instead.

Although not necessary in this case, you might further characterize the password by specifying additional attributes, such as the port number or the network protocol. For example, if you need to store distinct FTP and HTTP credentials for the same user working on the same server, you might add the [`kSecAttrProtocol`](ksecattrprotocol.md) attribute to distinguish between them.

Finally, the query contains the password from the user, encoded as a [`Data`](https://developer.apple.com/documentation/Foundation/Data) instance.

##### Add the Item

With the query complete, you simply feed it to the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function:

```swift
let status = SecItemAdd(query as CFDictionary, nil)
guard status == errSecSuccess else { throw KeychainError.unhandledError(status: status) }
```

Although you typically ignore the return data supplied by reference in the second argument on an add operation (as demonstrated here), always check the function’s return status to ensure that the operation succeeds. The operation might fail, for example, if an item with the given attributes already exists.

> **Note**:  If you do want the return data, keep in mind that the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function behaves much like the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function in this regard. See [`Searching for keychain items`](searching-for-keychain-items.md) for details.

 If you do want the return data, keep in mind that the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function behaves much like the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function in this regard. See [`Searching for keychain items`](searching-for-keychain-items.md) for details.

##### Ensure Searchability

To find the item later, use your knowledge of its attributes. In this example, the server and the account are the item’s distinguishing characteristics. For constant attributes (here, the server), use the same value during lookup. In contrast, the account attribute is dynamic, because it holds a value provided by the user at runtime. As long as your app never adds similar items with varying attributes (such as passwords for different accounts on the same server), you can omit these dynamic attributes as search parameters and instead retrieve them along with the item. As a result, when you look up the password, you also get the corresponding username. For more information on finding keychain items, see [`Searching for keychain items`](searching-for-keychain-items.md).

If your app does add items with varying dynamic attributes, you need a way to choose among them during retrieval. One option is to record information about the items in another way. For example, if you keep records of users in a Core Data model, you store the username there after using keychain services to store the password field. Later, you use the user name pulled from your data model to condition the search for the password.

In other cases, it might make sense to further characterize the item by adding more attributes. For example, you might include the [`kSecAttrLabel`](ksecattrlabel.md) attribute in the original add query, providing a string that marks the item for the particular purpose. Then you can use this attribute to narrow your search later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/adding-a-password-to-the-keychain)*