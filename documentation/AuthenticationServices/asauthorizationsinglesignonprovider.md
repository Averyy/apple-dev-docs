# ASAuthorizationSingleSignOnProvider

**Framework**: Authentication Services  
**Kind**: class

A mechanism for generating requests to authenticate users with third-party providers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationSingleSignOnProvider
```

## Topics

### Creating an Authorization Provider
- [convenience init(identityProvider: URL)](asauthorizationsinglesignonprovider/init(identityprovider:).md)
  Creates a single sign-on (SSO) authorization provider.
### Creating Authorization Requests
- [var canPerformAuthorization: Bool](asauthorizationsinglesignonprovider/canperformauthorization.md)
  A Boolean value that indicates if the provider is capable of performing authorization within a given configuration.
- [func createRequest() -> ASAuthorizationSingleSignOnRequest](asauthorizationsinglesignonprovider/createrequest.md)
  Creates a single sign-on (SSO) authorization request.
- [class ASAuthorizationSingleSignOnRequest](asauthorizationsinglesignonrequest.md)
  An OpenID authorization request that provides single sign-on (SSO) functionality.
- [class ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
  An OpenID authorization request.
### Identifying the Identity Provider
- [var url: URL](asauthorizationsinglesignonprovider/url.md)
  The URL of the identity provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ASAuthorizationSingleSignOnCredential](asauthorizationsinglesignoncredential.md)
  A credential that results from a successful single sign-on (SSO) authentication.
- [protocol ASAuthorizationProviderExtensionAuthorizationRequestHandler](asauthorizationproviderextensionauthorizationrequesthandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension handles authentication requests.
- [class ASAuthorizationProviderExtensionAuthorizationResult](asauthorizationproviderextensionauthorizationresult.md)
  The result of an authorization request.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignonprovider)*