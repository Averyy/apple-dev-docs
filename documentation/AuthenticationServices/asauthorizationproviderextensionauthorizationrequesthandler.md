# ASAuthorizationProviderExtensionAuthorizationRequestHandler

**Framework**: Authentication Services  
**Kind**: protocol

An interface through which a single sign-on (SSO) authentication provider extension handles authentication requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol ASAuthorizationProviderExtensionAuthorizationRequestHandler : NSObjectProtocol
```

## Topics

### Starting or Canceling a Request
- [func beginAuthorization(with: ASAuthorizationProviderExtensionAuthorizationRequest)](asauthorizationproviderextensionauthorizationrequesthandler/beginauthorization(with:).md)
  Tells your request handler to authorize the given request.
- [func cancelAuthorization(with: ASAuthorizationProviderExtensionAuthorizationRequest)](asauthorizationproviderextensionauthorizationrequesthandler/cancelauthorization(with:).md)
  Tells your request handler to cancel the authorization of the given request.
- [class ASAuthorizationProviderExtensionAuthorizationRequest](asauthorizationproviderextensionauthorizationrequest.md)
  An authorization request that your provider extension handles.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ASAuthorizationSingleSignOnProvider](asauthorizationsinglesignonprovider.md)
  A mechanism for generating requests to authenticate users with third-party providers.
- [class ASAuthorizationSingleSignOnCredential](asauthorizationsinglesignoncredential.md)
  A credential that results from a successful single sign-on (SSO) authentication.
- [class ASAuthorizationProviderExtensionAuthorizationResult](asauthorizationproviderextensionauthorizationresult.md)
  The result of an authorization request.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequesthandler)*