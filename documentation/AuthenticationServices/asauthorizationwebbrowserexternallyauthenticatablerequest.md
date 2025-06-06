# ASAuthorizationWebBrowserExternallyAuthenticatableRequest

**Framework**: Authentication Services  
**Kind**: protocol

An authorization request for which a web browser can retrieve credentials.

**Availability**:
- macOS 13.3+

## Declaration

```swift
protocol ASAuthorizationWebBrowserExternallyAuthenticatableRequest : NSObjectProtocol
```

## Topics

### Local authentication
- [var authenticatedContext: LAContext?](asauthorizationwebbrowserexternallyauthenticatablerequest/authenticatedcontext.md)
  The local authentication context for the authorization.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)

## See Also

- [protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialassertionrequest.md)
  An interface you use to respond to authentication challenges in a web browser.
- [protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest.md)
  An interface you use to respond to passkey-creation challenges in a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserexternallyauthenticatablerequest)*