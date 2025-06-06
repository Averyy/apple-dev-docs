# ASAuthorizationProviderExtensionAuthorizationResult

**Framework**: Authentication Services  
**Kind**: class

The result of an authorization request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionAuthorizationResult
```

## Topics

### Initializers
- [init(httpAuthorizationHeaders: [String : String])](asauthorizationproviderextensionauthorizationresult/init(httpauthorizationheaders:).md)
  Initializes an authorization with tokens stored in HTTP headers.
- [init(httpResponse: HTTPURLResponse, httpBody: Data?)](asauthorizationproviderextensionauthorizationresult/init(httpresponse:httpbody:).md)
  Initializes an authorization with a HTTP response and body.
### Instance Properties
- [var httpAuthorizationHeaders: [String : String]?](asauthorizationproviderextensionauthorizationresult/httpauthorizationheaders.md)
  A dictionary of authorization HTTP headers.
- [var httpResponse: HTTPURLResponse?](asauthorizationproviderextensionauthorizationresult/httpresponse.md)
  The HTTP response for authentications.
- [var httpBody: Data?](asauthorizationproviderextensionauthorizationresult/httpbody.md)
  The HTTP response body.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ASAuthorizationSingleSignOnProvider](asauthorizationsinglesignonprovider.md)
  A mechanism for generating requests to authenticate users with third-party providers.
- [class ASAuthorizationSingleSignOnCredential](asauthorizationsinglesignoncredential.md)
  A credential that results from a successful single sign-on (SSO) authentication.
- [protocol ASAuthorizationProviderExtensionAuthorizationRequestHandler](asauthorizationproviderextensionauthorizationrequesthandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension handles authentication requests.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationresult)*