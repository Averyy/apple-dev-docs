# SecPadding

**Framework**: Security  
**Kind**: struct

The types of padding to use when you create or verify a digital signature.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
struct SecPadding
```

## Topics

### Initializers
- [init(rawValue: UInt32)](secpadding/init(rawvalue:).md)
### Constants
- [static var sigRaw: SecPadding](secpadding/sigraw.md)
- [static var PKCS1: SecPadding](secpadding/pkcs1.md)
  PKCS1 padding.
- [static var OAEP: SecPadding](secpadding/oaep.md)
- [static var PKCS1MD2: SecPadding](secpadding/pkcs1md2.md)
  Data to be signed is an MD2 hash.
- [static var PKCS1MD5: SecPadding](secpadding/pkcs1md5.md)
  Data to be signed is an MD5 hash.
- [static var PKCS1SHA1: SecPadding](secpadding/pkcs1sha1.md)
  Data to be signed is a SHA1 hash.
- [static var PKCS1SHA224: SecPadding](secpadding/pkcs1sha224.md)
  Data to be signed is a SHA224 hash.
- [static var PKCS1SHA256: SecPadding](secpadding/pkcs1sha256.md)
  Data to be signed is a SHA256 hash.
- [static var PKCS1SHA384: SecPadding](secpadding/pkcs1sha384.md)
  Data to be signed is a SHA384 hash.
- [static var PKCS1SHA512: SecPadding](secpadding/pkcs1sha512.md)
  Data to be signed is a SHA512 hash.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding)*