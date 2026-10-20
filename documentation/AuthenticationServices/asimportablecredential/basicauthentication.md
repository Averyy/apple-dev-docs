# ASImportableCredential.BasicAuthentication

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A type to represent a basic authentication password.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct BasicAuthentication
```

#### Overview

This type is a representation of `BasicAuth` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Accessing authentication properties
- [var password: ASImportableEditableField?](./basicauthentication/password.md)
  The password associated with the credential.
- [struct ASImportableEditableField](../asimportableeditablefield.md)
  A field that someone can edit within a credential.
### Initializers
- [init(userName: ASImportableEditableField?, password: ASImportableEditableField?)](./basicauthentication/init%28username,password%29.md)
### Instance Properties
- [var userName: ASImportableEditableField?](./basicauthentication/username.md)
  The user name associated with this credential. When instantiating from JSON, this property will be populated from the “username” field.

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
- [case passkey(ASImportableCredential.Passkey)](./passkey%28_%29.md)
  A passkey credential.
- [ASImportableCredential.Passkey](./passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](./totp%28_%29.md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](./totp.md)
  A type to represent a time-based one-time password generator (TOTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/basicauthentication)*