# reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier:userHandle:acceptedCredentialIDs:)

**Framework**: Authentication Services  
**Kind**: method

Report a snapshot of all the credentialIDs that will be accepted for a `userHandle`. Credentials not present in the `acceptedCredentialIDs` may be removed or hidden by a password manager. Relying party may choose to perform this periodically, e.g. on every sign in. This information is shared with all password managers enabled in the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
final func reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier: String, userHandle: Data, acceptedCredentialIDs: [Data]) async throws
```

#### Discussion

> **Note**: `ASAuthorizationError` if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: Relying party (website) that the credential is saved for.
- `userHandle`: User identifier.
- `acceptedCredentialIDs`: An array of identifiers that uniquely identifies the accepted credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager/reportallacceptedpublickeycredentials(relyingpartyidentifier:userhandle:acceptedcredentialids:))*