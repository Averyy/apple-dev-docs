# reportPublicKeyCredentialUpdate(relyingPartyIdentifier:userHandle:newName:)

**Framework**: Authentication Services  
**Kind**: method

Report an update to a credential’s name, such as when changing the user name on an account. This information is shared with all password managers enabled in the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
final func reportPublicKeyCredentialUpdate(relyingPartyIdentifier: String, userHandle: Data, newName: String) async throws
```

#### Discussion

> **Note**: `ASAuthorizationError` if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: Relying party (website) that the credential is saved for.
- `userHandle`: User identifier.
- `newName`: The new user name for the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager/reportpublickeycredentialupdate(relyingpartyidentifier:userhandle:newname:))*