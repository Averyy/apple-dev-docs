# ASImportableCredential.TOTP.Algorithm

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

An enumeration of algorithm types that all importers are expected to support.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Algorithm
```

## Topics

### Algorithms
- [ASImportableCredential.TOTP.Algorithm.sha1](./algorithm-swift.enum/sha1.md)
  The SHA-1 algorithm.
- [ASImportableCredential.TOTP.Algorithm.sha256](./algorithm-swift.enum/sha256.md)
  The SHA-256 algorithm.
- [ASImportableCredential.TOTP.Algorithm.sha512](./algorithm-swift.enum/sha512.md)
  The SHA-512 algorithm.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing TOTP properties
- [var secret: Data](./secret.md)
  The secret associated with this generator.
- [var period: UInt16](./period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](./digits.md)
  The number of digits in the code used by the generator.
- [var algorithm: ASImportableCredential.TOTP.Algorithm](./algorithm-swift.property.md)
  The algorithm used by the generator.
- [var issuer: String?](./issuer.md)
  The issuer of the generator, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp/algorithm-swift.enum)*