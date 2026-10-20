# ASImportableCredential.TOTP

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A type to represent a time-based one-time password generator (TOTP).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct TOTP
```

#### Overview

This type is a representation of `TOTP` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Accessing TOTP properties
- [var secret: Data](./totp/secret.md)
  The secret associated with this generator.
- [var period: UInt16](./totp/period.md)
  The period, in seconds, used by the generator to refresh codes.
- [var digits: UInt16](./totp/digits.md)
  The number of digits in the code used by the generator.
- [var algorithm: ASImportableCredential.TOTP.Algorithm](./totp/algorithm-swift.property.md)
  The algorithm used by the generator.
- [ASImportableCredential.TOTP.Algorithm](./totp/algorithm-swift.enum.md)
  An enumeration of algorithm types that all importers are expected to support.
- [var issuer: String?](./totp/issuer.md)
  The issuer of the generator, if any.
### Initializers
- [init(secret: Data, period: UInt16, digits: UInt16, userName: String?, algorithm: ASImportableCredential.TOTP.Algorithm, issuer: String?)](./totp/init%28secret,period,digits,username,algorithm,issuer%29.md)
### Instance Properties
- [var userName: String?](./totp/username.md)
  The user name associated with the generator. When instantiating from JSON, this property will be populated from the “username” field.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Login credential types
- [case basicAuthentication(ASImportableCredential.BasicAuthentication)](./basicauthentication%28_%29.md)
  A password credential.
- [ASImportableCredential.BasicAuthentication](./basicauthentication.md)
  A type to represent a basic authentication password.
- [case passkey(ASImportableCredential.Passkey)](./passkey%28_%29.md)
  A passkey credential.
- [ASImportableCredential.Passkey](./passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](./totp%28_%29.md)
  A time-based one-time password (TOTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/totp)*