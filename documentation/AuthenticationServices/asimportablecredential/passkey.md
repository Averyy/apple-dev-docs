# ASImportableCredential.Passkey

**Framework**: Authentication Services  
**Kind**: struct

A type to represent a passkey credential.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Passkey
```

#### Overview

This type is a representation of `Passkey` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Creating a passkey instance
- [init(credentialID: Data, relyingPartyIdentifier: String, userName: String, userDisplayName: String, userHandle: Data, key: Data)](asimportablecredential/passkey/init(credentialid:relyingpartyidentifier:username:userdisplayname:userhandle:key:).md)
  Creates a passkey instance.
### Accessing passkey properties
- [var credentialID: Data](asimportablecredential/passkey/credentialid.md)
  The credential ID associated with this passkey.
- [var relyingPartyIdentifier: String](asimportablecredential/passkey/relyingpartyidentifier.md)
  The relying party identifier associated with the passkey.
- [var userName: String](asimportablecredential/passkey/username.md)
  The username associated with the passkey.
- [var userDisplayName: String](asimportablecredential/passkey/userdisplayname.md)
  The human-readable name associated with the passkey.
- [var userHandle: Data](asimportablecredential/passkey/userhandle.md)
  The user handle associated with the passkey.
- [var key: Data](asimportablecredential/passkey/key.md)
  The private key associated with this passkey.
### Initializers
- [init(credentialID: Data, relyingPartyIdentifier: String, userName: String, userDisplayName: String, userHandle: Data, key: Data, fido2Extensions: ASImportableFIDO2Extensions?)](asimportablecredential/passkey/init(credentialid:relyingpartyidentifier:username:userdisplayname:userhandle:key:fido2extensions:).md)
### Instance Properties
- [var fido2Extensions: ASImportableFIDO2Extensions?](asimportablecredential/passkey/fido2extensions.md)
  The FIDO2 extensions associated with this passkey.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case basicAuthentication(ASImportableCredential.BasicAuthentication)](asimportablecredential/basicauthentication(_:).md)
  A password credential.
- [ASImportableCredential.BasicAuthentication](asimportablecredential/basicauthentication.md)
  A type to represent a basic authentication password.
- [case passkey(ASImportableCredential.Passkey)](asimportablecredential/passkey(_:).md)
  A passkey credential.
- [case totp(ASImportableCredential.TOTP)](asimportablecredential/totp(_:).md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](asimportablecredential/totp.md)
  A type to represent a time-based one-time password generator (TOTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/passkey)*