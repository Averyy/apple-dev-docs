# createCredentialRegistrationRequest(challenge:name:userID:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Creates a registration request with a challenge, name, and user ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

```objc
- (ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest *) createCredentialRegistrationRequestWithChallenge:(NSData *) challenge name:(NSString *) name userID:(NSData *) userID;
```

## Return Value

A public key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.
- `name`: The name of the user.
- `userID`: A user identifier.

## See Also

### Creating the request
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,name,userid,requeststyle%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:))*