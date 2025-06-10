# algorithm

**Framework**: Authentication Services  
**Kind**: property

The algorithm used by the generator.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var algorithm: ASImportableCredential.TOTP.Algorithm
```

#### Discussion

This value must be one of [`ASImportableCredential.TOTP.Algorithm.sha1`](asimportablecredential/totp/algorithm-swift.enum/sha1.md), [`ASImportableCredential.TOTP.Algorithm.sha256`](asimportablecredential/totp/algorithm-swift.enum/sha256.md), or [`ASImportableCredential.TOTP.Algorithm.sha512`](asimportablecredential/totp/algorithm-swift.enum/sha512.md).

## See Also

- [var secret: Data](asimportablecredential/totp/secret.md)
  The secret associated with this generator.
- [var period: UInt16](asimportablecredential/totp/period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](asimportablecredential/totp/digits.md)
  The number of digits in the code used by the generator.
- [ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.enum.md)
  An enumeration of algorithm types that all importers are expected to support.
- [var issuer: String?](asimportablecredential/totp/issuer.md)
  The issuer of the generator, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp/algorithm-swift.property)*