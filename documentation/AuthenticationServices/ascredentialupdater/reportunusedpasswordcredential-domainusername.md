# reportUnusedPasswordCredential(domain:userName:)

**Framework**: Authentication Services  
**Kind**: method

Informs credential managers that a password is no longer in use.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func reportUnusedPasswordCredential(domain: String, userName: String) async throws
```

#### Discussion

Credential managers can act on this report by removing or hiding the password credential.

This call shares the updated credential data with all enabled credential managers installed on the system.

> **Note**: This method throws [`ASAuthorizationError`](asauthorizationerror-swift.struct.md) if the system failed to accept the update. ` if the system failed to accept the update.

## Parameters

- `domain`: The website domain for which to save the password.
- `userName`: The account user name.

## See Also

- [func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws](ascredentialupdater/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:).md)
  Informs credential managers that a specific credential is unknown or no longer accepted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater/reportunusedpasswordcredential(domain:username:))*