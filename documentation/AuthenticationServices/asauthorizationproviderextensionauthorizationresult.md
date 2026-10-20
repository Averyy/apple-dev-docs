# ASAuthorizationProviderExtensionAuthorizationResult

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationProviderExtensionAuthorizationResult : NSObject
```

## Topics

### Initializers
- [init(httpAuthorizationHeaders: [String : String])](./asauthorizationproviderextensionauthorizationresult/init%28httpauthorizationheaders%29-ywja.md)
  Initializes an authorization with tokens stored in HTTP headers.
- [init(httpResponse: HTTPURLResponse, httpBody: Data?)](./asauthorizationproviderextensionauthorizationresult/init%28httpresponse,httpbody%29-2j92m.md)
  Initializes an authorization with a HTTP response and body.
- [init(HTTPAuthorizationHeaders: [String : String])](./asauthorizationproviderextensionauthorizationresult/init%28httpauthorizationheaders%29-932pm.md)
- [init(HTTPResponse: HTTPURLResponse, httpBody: Data?)](./asauthorizationproviderextensionauthorizationresult/init%28httpresponse,httpbody%29-48yla.md)
### Instance Properties
- [var httpAuthorizationHeaders: [String : String]?](./asauthorizationproviderextensionauthorizationresult/httpauthorizationheaders.md)
  A dictionary of authorization HTTP headers.
- [var httpResponse: HTTPURLResponse?](./asauthorizationproviderextensionauthorizationresult/httpresponse.md)
  The HTTP response for authentications.
- [var httpBody: Data?](./asauthorizationproviderextensionauthorizationresult/httpbody.md)
  The HTTP response body.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing enterprise single sign-on
- [class ASAuthorizationSingleSignOnProvider](./asauthorizationsinglesignonprovider.md)
  A mechanism for generating requests to authenticate users with third-party providers.
- [class ASAuthorizationSingleSignOnCredential](./asauthorizationsinglesignoncredential.md)
  A credential that results from a successful single sign-on (SSO) authentication.
- [protocol ASAuthorizationProviderExtensionAuthorizationRequestHandler](./asauthorizationproviderextensionauthorizationrequesthandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension handles authentication requests.
- [ASAuthorizationController.RequestOptions](./asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationresult)*