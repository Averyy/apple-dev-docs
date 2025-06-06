# createCredentialAssertionRequest(challenge:)

**Framework**: Authentication Services  
**Kind**: method

Creates an assertion request with a challenge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest
```

#### Return Value

A security key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.

## See Also

- [var relyingPartyIdentifier: String](asauthorizationsecuritykeypublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to authorize against.
- [func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialprovider/createcredentialregistrationrequest(challenge:displayname:name:userid:).md)
  Creates an assertion request with a challenge, display name, and user ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider/createcredentialassertionrequest(challenge:))*