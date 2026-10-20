# SecPadding

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

The types of padding to use when you create or verify a digital signature.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.6+ - Deprecated in 12.0
- tvOS 4.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Replaced with SecKeyAlgorithm

## Declaration

```swift
struct SecPadding
```

```c
enum SecPadding : uint32_t;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./secpadding/init%28rawvalue%29.md)
### Constants
- [static var sigRaw: SecPadding](./secpadding/sigraw.md)
- [static var PKCS1: SecPadding](./secpadding/pkcs1.md)
  PKCS1 padding.
- [static var OAEP: SecPadding](./secpadding/oaep.md)
- [static var PKCS1MD2: SecPadding](./secpadding/pkcs1md2.md)
  Data to be signed is an MD2 hash.
- [static var PKCS1MD5: SecPadding](./secpadding/pkcs1md5.md)
  Data to be signed is an MD5 hash.
- [static var PKCS1SHA1: SecPadding](./secpadding/pkcs1sha1.md)
  Data to be signed is a SHA1 hash.
- [static var PKCS1SHA224: SecPadding](./secpadding/pkcs1sha224.md)
  Data to be signed is a SHA224 hash.
- [static var PKCS1SHA256: SecPadding](./secpadding/pkcs1sha256.md)
  Data to be signed is a SHA256 hash.
- [static var PKCS1SHA384: SecPadding](./secpadding/pkcs1sha384.md)
  Data to be signed is a SHA384 hash.
- [static var PKCS1SHA512: SecPadding](./secpadding/pkcs1sha512.md)
  Data to be signed is a SHA512 hash.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding)*