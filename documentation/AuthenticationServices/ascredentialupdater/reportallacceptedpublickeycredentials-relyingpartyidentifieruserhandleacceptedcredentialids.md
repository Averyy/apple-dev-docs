# reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier:userHandle:acceptedCredentialIDs:)

**Framework**: Authentication Services  
**Kind**: method

Provides credential managers with a snapshot of all credential identifiers accepted for a given user handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier: String, userHandle: Data, acceptedCredentialIDs: [Data]) async throws
```

#### Discussion

If your app allows someone to revoke a passkey or create a new one, call this method to report all credentials still accepted after the change. Credential managers can act on this report by removing or hiding any credentials not present in `acceptedCredentialIDs`, which prevents display of invalid passkeys during later sign ins.

You can also call this method periodically, such as by invoking it on every sign in. This sort of periodic check in helps keep credential managers up to date.

This call shares the updated credential data with all enabled credential managers installed on the system.

> **Note**: This method throws [`ASAuthorizationError`](asauthorizationerror-swift.struct.md) if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: The relying party, typically a website, for which to save the credential.
- `userHandle`: The user identifier.
- `acceptedCredentialIDs`: An array of identifiers that uniquely identifies the accepted credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater/reportallacceptedpublickeycredentials(relyingpartyidentifier:userhandle:acceptedcredentialids:))*