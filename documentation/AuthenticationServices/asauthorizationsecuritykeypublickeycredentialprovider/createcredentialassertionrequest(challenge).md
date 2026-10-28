# createCredentialAssertionRequest(challenge:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest *) createCredentialAssertionRequestWithChallenge:(NSData *) challenge;
```

## Return Value

A security key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.

## See Also

### Creating the request
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the service to authorize against.
- [func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,displayname,name,userid%29.md)
  Creates a registration request with a challenge, display name, and user ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider/createcredentialassertionrequest(challenge:))*