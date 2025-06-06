# ASAuthorizationSingleSignOnCredential

**Framework**: Authentication Services  
**Kind**: class

A credential that results from a successful single sign-on (SSO) authentication.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationSingleSignOnCredential
```

## Topics

### Identifying a User
- [var identityToken: Data?](asauthorizationsinglesignoncredential/identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to your app.
- [var accessToken: Data?](asauthorizationsinglesignoncredential/accesstoken.md)
  An access token used to get an identity token.
- [var state: String?](asauthorizationsinglesignoncredential/state.md)
  An arbitrary string that your app provided to the request that generated this credential.
- [var authorizedScopes: [ASAuthorization.Scope]](asauthorizationsinglesignoncredential/authorizedscopes.md)
  The contact information the user authorized your app to access.
### Parsing the Response
- [var authenticatedResponse: HTTPURLResponse?](asauthorizationsinglesignoncredential/authenticatedresponse.md)
  The complete response authentication, including technology-specific values.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ASAuthorizationSingleSignOnProvider](asauthorizationsinglesignonprovider.md)
  A mechanism for generating requests to authenticate users with third-party providers.
- [protocol ASAuthorizationProviderExtensionAuthorizationRequestHandler](asauthorizationproviderextensionauthorizationrequesthandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension handles authentication requests.
- [class ASAuthorizationProviderExtensionAuthorizationResult](asauthorizationproviderextensionauthorizationresult.md)
  The result of an authorization request.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsinglesignoncredential)*