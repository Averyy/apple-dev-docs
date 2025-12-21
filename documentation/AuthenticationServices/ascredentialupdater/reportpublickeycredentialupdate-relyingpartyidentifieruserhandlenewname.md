# reportPublicKeyCredentialUpdate(relyingPartyIdentifier:userHandle:newName:)

**Framework**: Authentication Services  
**Kind**: method

Provides credential managers with an update to a credential’s name, such as when changing the user name or email address on an account.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func reportPublicKeyCredentialUpdate(relyingPartyIdentifier: String, userHandle: Data, newName: String) async throws
```

#### Discussion

This call shares the updated credential data with all credential managers installed on the system.

> **Note**: This method throws [`ASAuthorizationError`](asauthorizationerror-swift.struct.md) if the system failed to accept the update.

## Parameters

- `relyingPartyIdentifier`: The relying party, typically a website, for which to save the credential.
- `userHandle`: The user identifier.
- `newName`: The new user name for the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater/reportpublickeycredentialupdate(relyingpartyidentifier:userhandle:newname:))*