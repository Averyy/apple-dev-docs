# SecAccessCreate(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new access instance associated with a given protected keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecAccessCreate(_ descriptor: CFString, _ trustedlist: CFArray?, _ accessRef: UnsafeMutablePointer<SecAccess?>) -> OSStatus
```

#### Return Value

[`errSecSuccess`](errsecsuccess.md) on success, or another status result on failure. See [`Security Framework Result Codes`](security-framework-result-codes.md) for all possible status results.

#### Discussion

Use this method to create a default access instance containing three ACL entries. If you don’t explicitly create and set an access instance when you create a protected keychain item, keychain services uses a default access like this one.

![Diagram showing the contents of the default access instance, including three entries, each with specific operations and trusted apps.](https://docs-assets.developer.apple.com/published/7bb43362f99e782e9a44a92221966583/media-2983147%402x.png)

-  Determines who can modify the access instance, because it contains the [`kSecACLAuthorizationChangeACL`](ksecaclauthorizationchangeacl.md) authorization. The owner entry’s list of trusted apps is empty, so the user is always prompted for permission if someone tries to change the access instance. All access instances must have exactly one owner entry, so this item can’t be removed, although you can modify it.
-  Applies to operations not considered secure, namely encrypting data. This ACL entry trusts all apps by default, because its array of trusted apps is set to `nil`.
-  Applies to operations that are considered sensitive, such as decrypting, signing, deriving keys, and exporting keys. The method applies the list of apps given in the `trustedlist` parameter to this entry. If you set `trustedlist` to `nil`, the list of trusted apps contains only the calling app.

##### Retrieving and Modifying Acl Entries

After you (or keychain services) create the access instance, you can retrieve all its ACL entries using the [`SecAccessCopyACLList(_:_:)`](secaccesscopyacllist(_:_:).md) method. You can then modify any of these entries using the [`SecACLSetContents(_:_:_:_:)`](secaclsetcontents(_:_:_:_:).md) method, or modify the operations for which an ACL entry is used using the [`SecACLUpdateAuthorizations(_:_:)`](secaclupdateauthorizations(_:_:).md) method. You can also create additional ACL entries using the [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](secaclcreatewithsimplecontents(_:_:_:_:_:).md) method. Because an ACL is always associated with an access instance, when you modify an entry or create a new one, you’re implicitly modifying the access instance as well.

You then apply the fully configured access instance to a keychain item by setting it as the item’s [`kSecAttrAccess`](ksecattraccess.md) attribute. See [`Keychain items`](keychain-items.md) for details about creating and modifying keychain items.

## Parameters

- `descriptor`: This isn’t necessarily the name that appears in the Keychain Access app.
- `trustedlist`: Use   to trust only the calling app. Use an empty array to indicate no apps are trusted.
- `accessRef`: On return, points to the new access instance. In Objective-C, call   to release this instance when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscreate(_:_:_:))*