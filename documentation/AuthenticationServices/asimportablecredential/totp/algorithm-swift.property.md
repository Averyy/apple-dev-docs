# algorithm

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The algorithm used by the generator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var algorithm: ASImportableCredential.TOTP.Algorithm
```

#### Discussion

This value must be one of [`ASImportableCredential.TOTP.Algorithm.sha1`](./algorithm-swift.enum/sha1.md), [`ASImportableCredential.TOTP.Algorithm.sha256`](./algorithm-swift.enum/sha256.md), or [`ASImportableCredential.TOTP.Algorithm.sha512`](./algorithm-swift.enum/sha512.md).

## See Also

### Accessing TOTP properties
- [var secret: Data](./secret.md)
  The secret associated with this generator.
- [var period: UInt16](./period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](./digits.md)
  The number of digits in the code used by the generator.
- [ASImportableCredential.TOTP.Algorithm](./algorithm-swift.enum.md)
  An enumeration of algorithm types that all importers are expected to support.
- [var issuer: String?](./issuer.md)
  The issuer of the generator, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp/algorithm-swift.property)*