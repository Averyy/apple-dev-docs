# ASImportableCredential.Passkey

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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

## Overview

This type is a representation of `Passkey` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Creating a passkey instance
- [init(credentialID: Data, relyingPartyIdentifier: String, userName: String, userDisplayName: String, userHandle: Data, key: Data)](./passkey/init%28credentialid,relyingpartyidentifier,username,userdisplayname,userhandle,key%29.md)
  Creates a passkey instance.
### Accessing passkey properties
- [var credentialID: Data](./passkey/credentialid.md)
  The credential ID associated with this passkey.
- [var relyingPartyIdentifier: String](./passkey/relyingpartyidentifier.md)
  The relying party identifier associated with the passkey.
- [var userName: String](./passkey/username.md)
  The username associated with the passkey.
- [var userDisplayName: String](./passkey/userdisplayname.md)
  The human-readable name associated with the passkey.
- [var userHandle: Data](./passkey/userhandle.md)
  The user handle associated with the passkey.
- [var key: Data](./passkey/key.md)
  The private key associated with this passkey.
### Initializers
- [init(credentialID: Data, relyingPartyIdentifier: String, userName: String, userDisplayName: String, userHandle: Data, key: Data, fido2Extensions: ASImportableFIDO2Extensions?)](./passkey/init%28credentialid,relyingpartyidentifier,username,userdisplayname,userhandle,key,fido2extensions%29.md)
### Instance Properties
- [var fido2Extensions: ASImportableFIDO2Extensions?](./passkey/fido2extensions.md)
  The FIDO2 extensions associated with this passkey.

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
- [case totp(ASImportableCredential.TOTP)](./totp%28_%29.md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](./totp.md)
  A type to represent a time-based one-time password generator (TOTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/passkey)*