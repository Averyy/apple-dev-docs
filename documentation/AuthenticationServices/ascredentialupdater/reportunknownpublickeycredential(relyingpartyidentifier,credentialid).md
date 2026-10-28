# reportUnknownPublicKeyCredential(relyingPartyIdentifier:credentialID:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Informs credential managers that a specific credential is unknown or no longer accepted.

**Availability**:
- iOS 26.0+ - Deprecated in 26.2
- iPadOS 26.0+ - Deprecated in 26.2
- Mac Catalyst 26.0+ - Deprecated in 26.2
- macOS 26.0+ - Deprecated in 26.2
- visionOS 26.0+ - Deprecated in 26.2

> **Deprecated**: Use `ASCredentialDataManager` instead

## Declaration

```swift
final func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws
```

## Discussion

Credential managers can act on this report by removing or hiding the credential.

This call shares the updated credential data with all credential managers installed on the system.

> **Throws**: This method throws [`ASAuthorizationError`](../asauthorizationerror-swift.struct.md) if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: The relying party, typically a website, for which to update the credential.
- `credentialID`: An identifier that uniquely identifies this credential.

## See Also

### Reporting unused and unknown credentials
- [func reportUnusedPasswordCredential(domain: String, userName: String) async throws](./reportunusedpasswordcredential%28domain,username%29.md)
  Informs credential managers that a password is no longer in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:))*