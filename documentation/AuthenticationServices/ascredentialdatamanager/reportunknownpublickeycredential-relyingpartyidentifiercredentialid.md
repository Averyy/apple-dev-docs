# reportUnknownPublicKeyCredential(relyingPartyIdentifier:credentialID:)

**Framework**: Authentication Services  
**Kind**: method

Report that a specific credential is unknown or no longer accepted. The credential may be removed or hidden by a password manager. This information is shared with all password managers enabled in the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
final func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws
```

#### Discussion

> **Note**: `ASAuthorizationError` if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: Relying party (website) that the credential is saved for.
- `credentialID`: An identifier that uniquely identifies this credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:))*