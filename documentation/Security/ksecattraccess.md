# kSecAttrAccess

**Framework**: Security  
**Kind**: var

A key with a value that indicates access control list settings for the item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecAttrAccess: CFString
```

#### Discussion

The corresponding value is a [`SecAccess`](secaccess.md) instance that describes the access control settings for this item. Create an access instance by calling the [`SecAccessCreate(_:_:_:)`](secaccesscreate(_:_:_:).md) method. For more information, see [`Access Control Lists`](access-control-lists.md).

Use this attribute to set an access instance when you:

- Create a keychain item, by adding the `kSecAttrAccess` key to the dictionary you pass to [`SecItemAdd(_:_:)`](secitemadd(_:_:).md).
- Modify a keychain item, by adding the `kSecAttrAccess` key to the dictionary you pass as the second parameter to [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md).

You can’t use this attribute to:

- Search for an item by its access instance; for example, by adding `kSecAttrAccess` to the dictionary you pass as the first parameter to [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md). [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) and [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) ignore this key when searching for keychain items.
- Get an item’s access instance with [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md). To get an item’s access instance, call [`SecKeychainItemCopyAccess(_:_:)`](seckeychainitemcopyaccess(_:_:).md).

> ❗ **Important**:  This attribute is mutually exclusive with the [`kSecAttrAccessControl`](ksecattraccesscontrol.md) attribute. Also, it only applies to keychain items stored in macOS that don’t have one or both of the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) or [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) keys set to `true`. For information on access control for other keychain items, see [`Sharing access to keychain items among a collection of apps`](sharing-access-to-keychain-items-among-a-collection-of-apps.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccess)*