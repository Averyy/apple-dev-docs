# createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

```objc
- (ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest *) createCredentialRegistrationRequestWithChallenge:(NSData *) challenge name:(NSString *) name userID:(NSData *) userID requestStyle:(ASAuthorizationPlatformPublicKeyCredentialRegistrationRequestStyle) requestStyle;
```

## Discussion

Create a request to register a new platform credential.

## Parameters

- `challenge`: The challenge to sign.
- `name`: The user name for the new credential.
- `userID`: An identifier to be stored alongside the credential, which will be returned with the credential when it is used to authenticate.
- `requestStyle`: The style for this request.

## See Also

### Creating the request
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,name,userid%29.md)
  Creates a registration request with a challenge, name, and user ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:requeststyle:))*