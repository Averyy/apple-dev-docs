# ASImportableCredential.TOTP

**Framework**: Authentication Services  
**Kind**: struct

A type to represent a time-based one-time password generator (TOTP).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct TOTP
```

#### Overview

This type is a representation of `TOTP` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Accessing TOTP properties
- [var secret: Data](asimportablecredential/totp/secret.md)
  The secret associated with this generator.
- [var period: UInt16](asimportablecredential/totp/period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](asimportablecredential/totp/digits.md)
  The number of digits in the code used by the generator.
- [var algorithm: ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.property.md)
  The algorithm used by the generator.
- [ASImportableCredential.TOTP.Algorithm](asimportablecredential/totp/algorithm-swift.enum.md)
  An enumeration of algorithm types that all importers are expected to support.
- [var issuer: String?](asimportablecredential/totp/issuer.md)
  The issuer of the generator, if any.
### Initializers
- [init(secret: Data, period: UInt16, digits: UInt16, userName: String?, algorithm: ASImportableCredential.TOTP.Algorithm, issuer: String?)](asimportablecredential/totp/init(secret:period:digits:username:algorithm:issuer:).md)
### Instance Properties
- [var userName: String?](asimportablecredential/totp/username.md)
  The user name associated with the generator.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case basicAuthentication(ASImportableCredential.BasicAuthentication)](asimportablecredential/basicauthentication(_:).md)
  A password credential.
- [ASImportableCredential.BasicAuthentication](asimportablecredential/basicauthentication.md)
  A type to represent a basic authentication password.
- [case passkey(ASImportableCredential.Passkey)](asimportablecredential/passkey(_:).md)
  A passkey credential.
- [ASImportableCredential.Passkey](asimportablecredential/passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](asimportablecredential/totp(_:).md)
  A time-based one-time password (TOTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp)*