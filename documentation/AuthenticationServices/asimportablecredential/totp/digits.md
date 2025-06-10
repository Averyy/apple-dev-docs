# digits

**Framework**: Authentication Services  
**Kind**: property

The number of digits in the code used by the generator.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var digits: UInt16
```

## See Also

- [var secret: Data](asimportablecredential/totp/secret.md)
  The secret associated with this generator.
- [var period: UInt16](asimportablecredential/totp/period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var algorithm: ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.property.md)
  The algorithm used by the generator.
- [ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.enum.md)
  An enumeration of algorithm types that all importers are expected to support.
- [var issuer: String?](asimportablecredential/totp/issuer.md)
  The issuer of the generator, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp/digits)*