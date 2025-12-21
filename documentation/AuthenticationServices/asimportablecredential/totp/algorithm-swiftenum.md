# ASImportableCredential.TOTP.Algorithm

**Framework**: Authentication Services  
**Kind**: enum

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
- [ASImportableCredential.TOTP.Algorithm.sha1](asimportablecredential/totp/algorithm-swift.enum/sha1.md)
  The SHA-1 algorithm.
- [ASImportableCredential.TOTP.Algorithm.sha256](asimportablecredential/totp/algorithm-swift.enum/sha256.md)
  The SHA-256 algorithm.
- [ASImportableCredential.TOTP.Algorithm.sha512](asimportablecredential/totp/algorithm-swift.enum/sha512.md)
  The SHA-512 algorithm.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var secret: Data](asimportablecredential/totp/secret.md)
  The secret associated with this generator.
- [var period: UInt16](asimportablecredential/totp/period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](asimportablecredential/totp/digits.md)
  The number of digits in the code used by the generator.
- [var algorithm: ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.property.md)
  The algorithm used by the generator.
- [var issuer: String?](asimportablecredential/totp/issuer.md)
  The issuer of the generator, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp/algorithm-swift.enum)*