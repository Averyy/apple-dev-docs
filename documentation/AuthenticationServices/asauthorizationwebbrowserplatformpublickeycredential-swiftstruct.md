# ASAuthorizationWebBrowserPlatformPublicKeyCredential

**Framework**: Authentication Services  
**Kind**: struct

A structure that describes a passkey stored in the keychain, or managed by a third-party credential manager.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
struct ASAuthorizationWebBrowserPlatformPublicKeyCredential
```

#### Overview

Use [`ASAuthorizationWebBrowserPlatformPublicKeyCredential`](asauthorizationwebbrowserplatformpublickeycredential-swift.struct.md) to describe passkeys in your browser app’s user interface so the person can choose a passkey. Get the chosen passkey’s [`credentialID`](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/credentialid.md) to create a [`ASAuthorizationPlatformPublicKeyCredentialDescriptor`](asauthorizationplatformpublickeycredentialdescriptor.md) that identifies the passkey to the operating system.

## Topics

### Describing credentials
- [let customTitle: String](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/customtitle.md)
  A string the person can supply to describe this credential.
- [let name: String](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/name.md)
  The user name for the account associated with this credential.
- [let providerName: String](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/providername.md)
  The name of the app that manages this credential, or “iCloud Keychain” if it’s the operating system.
- [let relyingParty: String](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/relyingparty.md)
  The relying party that issues challenges for this credential.
- [let userHandle: Data](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/userhandle.md)
  A unique identifier for the user account at the relying party.
### Identifying credentials
- [let credentialID: Data](asauthorizationwebbrowserplatformpublickeycredential-swift.struct/credentialid.md)
  The identifier the operating system uses for this credential.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func platformCredentials(forRelyingParty: String) async -> [ASAuthorizationWebBrowserPlatformPublicKeyCredential]](asauthorizationwebbrowserpublickeycredentialmanager/platformcredentials(forrelyingparty:).md)
  Gets a list of passkeys available for authenticating with the given relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredential-swift.struct)*