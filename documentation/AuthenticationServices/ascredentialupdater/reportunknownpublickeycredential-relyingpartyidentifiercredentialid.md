# reportUnknownPublicKeyCredential(relyingPartyIdentifier:credentialID:)

**Framework**: Authentication Services  
**Kind**: method

Informs credential managers that a specific credential is unknown or no longer accepted.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws
```

#### Discussion

Credential managers can act on this report by removing or hiding the credential.

This call shares the updated credential data with all credential managers installed on the system.

> **Note**: This method throws [`ASAuthorizationError`](asauthorizationerror-swift.struct.md) if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: The relying party, typically a website, for which to update the credential.
- `credentialID`: An identifier that uniquely identifies this credential.

## See Also

- [func reportUnusedPasswordCredential(domain: String, userName: String) async throws](ascredentialupdater/reportunusedpasswordcredential(domain:username:).md)
  Informs credential managers that a password is no longer in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:))*