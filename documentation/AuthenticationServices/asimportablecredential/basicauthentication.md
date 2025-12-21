# ASImportableCredential.BasicAuthentication

**Framework**: Authentication Services  
**Kind**: struct

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
- [var password: ASImportableEditableField?](asimportablecredential/basicauthentication/password.md)
  The password associated with the credential.
- [struct ASImportableEditableField](asimportableeditablefield.md)
  A field that someone can edit within a credential.
### Initializers
- [init(userName: ASImportableEditableField?, password: ASImportableEditableField?)](asimportablecredential/basicauthentication/init(username:password:).md)
### Instance Properties
- [var userName: ASImportableEditableField?](asimportablecredential/basicauthentication/username.md)
  The user name associated with this credential. When instantiating from JSON, this property will be populated from the “username” field.

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
- [case passkey(ASImportableCredential.Passkey)](asimportablecredential/passkey(_:).md)
  A passkey credential.
- [ASImportableCredential.Passkey](asimportablecredential/passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](asimportablecredential/totp(_:).md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](asimportablecredential/totp.md)
  A type to represent a time-based one-time password generator (TOTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/basicauthentication)*