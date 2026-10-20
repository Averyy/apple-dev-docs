# relyingPartyIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The domain name of the service to register or authorize against.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var relyingPartyIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * relyingPartyIdentifier;
```

## See Also

### Creating the request
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,name,userid%29.md)
  Creates a registration request with a challenge, name, and user ID.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,name,userid,requeststyle%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/relyingpartyidentifier)*