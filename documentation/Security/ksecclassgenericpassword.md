# kSecClassGenericPassword

**Framework**: Security  
**Kind**: var

The value that indicates a generic password item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecClassGenericPassword: CFString
```

## Mentions

- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)

#### Discussion

The following keychain item attributes form the composite primary key of a generic password item:

- [`kSecAttrAccessGroup`](ksecattraccessgroup.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/Swift/true))
- [`kSecAttrAccount`](ksecattraccount.md)
- [`kSecAttrService`](ksecattrservice.md)
- [`kSecAttrSynchronizable`](ksecattrsynchronizable.md)

Calls to [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) that add a generic password item with the same values for all of these attributes as an existing item result in [`errSecDuplicateItem`](errsecduplicateitem.md).

The following keychain item attributes apply to a generic password item, and don’t form part of its composite primary key:

- [`kSecAttrAccess`](ksecattraccess.md) (macOS only)
- [`kSecAttrAccessControl`](ksecattraccesscontrol.md)
- [`kSecAttrAccessible`](ksecattraccessible.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/Swift/true))
- [`kSecAttrCreationDate`](ksecattrcreationdate.md)
- [`kSecAttrModificationDate`](ksecattrmodificationdate.md)
- [`kSecAttrDescription`](ksecattrdescription.md)
- [`kSecAttrComment`](ksecattrcomment.md)
- [`kSecAttrCreator`](ksecattrcreator.md)
- [`kSecAttrType`](ksecattrtype.md)
- [`kSecAttrLabel`](ksecattrlabel.md)
- [`kSecAttrIsInvisible`](ksecattrisinvisible.md)
- [`kSecAttrIsNegative`](ksecattrisnegative.md)
- [`kSecAttrGeneric`](ksecattrgeneric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecclassgenericpassword)*