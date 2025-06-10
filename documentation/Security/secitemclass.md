# SecItemClass

**Framework**: Security  
**Kind**: enum

Specifies a keychain item’s class code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecItemClass
```

#### Overview

These enumerations define constants your application can use to specify the type of the keychain item you wish to create, dispose, add, delete, update, copy, or locate. You can also use these constants with the tag constant [`SecItemAttr`](secitemattr.md).

## Topics

### Constants
- [SecItemClass.internetPasswordItemClass](secitemclass/internetpassworditemclass.md)
  Indicates that the item is an Internet password.
- [SecItemClass.genericPasswordItemClass](secitemclass/genericpassworditemclass.md)
  Indicates that the item is a generic password.
- [SecItemClass.certificateItemClass](secitemclass/certificateitemclass.md)
  Indicates that the item is an X509 certificate.
- [SecItemClass.publicKeyItemClass](secitemclass/publickeyitemclass.md)
  Indicates that the item is a public key of a public-private pair.
- [SecItemClass.privateKeyItemClass](secitemclass/privatekeyitemclass.md)
  Indicates that the item is a private key of a public-private pair.
- [SecItemClass.symmetricKeyItemClass](secitemclass/symmetrickeyitemclass.md)
  Indicates that the item is a private key used for symmetric-key encryption.
### Initializers
- [init?(rawValue: FourCharCode)](secitemclass/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemclass)*