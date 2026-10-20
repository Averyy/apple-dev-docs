# SecItemClass

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

Specifies a keychain item’s class code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecItemClass
```

```c
enum SecItemClass : FourCharCode;
```

#### Overview

These enumerations define constants your application can use to specify the type of the keychain item you wish to create, dispose, add, delete, update, copy, or locate. You can also use these constants with the tag constant [`SecItemAttr`](./secitemattr.md).

## Topics

### Constants
- [SecItemClass.internetPasswordItemClass](./secitemclass/internetpassworditemclass.md)
  Indicates that the item is an Internet password.
- [SecItemClass.genericPasswordItemClass](./secitemclass/genericpassworditemclass.md)
  Indicates that the item is a generic password.
- [SecItemClass.certificateItemClass](./secitemclass/certificateitemclass.md)
  Indicates that the item is an X509 certificate.
- [SecItemClass.publicKeyItemClass](./secitemclass/publickeyitemclass.md)
  Indicates that the item is a public key of a public-private pair.
- [SecItemClass.privateKeyItemClass](./secitemclass/privatekeyitemclass.md)
  Indicates that the item is a private key of a public-private pair.
- [SecItemClass.symmetricKeyItemClass](./secitemclass/symmetrickeyitemclass.md)
  Indicates that the item is a private key used for symmetric-key encryption.
### Initializers
- [init?(rawValue: FourCharCode)](./secitemclass/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemclass)*