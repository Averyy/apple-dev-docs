# relyingPartyIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The domain name of the service to authorize against.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var relyingPartyIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * relyingPartyIdentifier;
```

## See Also

### Creating the request
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28challenge,displayname,name,userid%29.md)
  Creates a registration request with a challenge, display name, and user ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider/relyingpartyidentifier)*