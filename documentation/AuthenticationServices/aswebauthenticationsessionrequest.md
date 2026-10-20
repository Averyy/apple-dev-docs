# ASWebAuthenticationSessionRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A login session request that a web browser receives from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class ASWebAuthenticationSessionRequest
```

```objc
@interface ASWebAuthenticationSessionRequest : NSObject
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](./supporting-single-sign-on-in-a-web-browser-app.md)

## Topics

### Interpreting a request
- [var url: URL](./aswebauthenticationsessionrequest/url.md)
  The web address the browser should use to perform the authentication request.
- [var shouldUseEphemeralSession: Bool](./aswebauthenticationsessionrequest/shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var uuid: UUID](./aswebauthenticationsessionrequest/uuid.md)
  A unique identifier for the request.
- [var additionalHeaderFields: [String : String]?](./aswebauthenticationsessionrequest/additionalheaderfields.md)
  Additional headers to send when loading the initial URL.
### Finishing a request
- [var callback: ASWebAuthenticationSession.Callback?](./aswebauthenticationsessionrequest/callback.md)
  The callback to listen for, which completes the request.
- [ASWebAuthenticationSession.Callback](./aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func complete(withCallbackURL: URL)](./aswebauthenticationsessionrequest/complete%28withcallbackurl%29.md)
  Indicates that the browser successfully completed the authentication attempt.
- [func cancelWithError(any Error)](./aswebauthenticationsessionrequest/cancelwitherror%28_%29.md)
  Indicates that the browser canceled the authentication attempt.
### Indicating completion
- [var delegate: (any ASWebAuthenticationSessionRequestDelegate)?](./aswebauthenticationsessionrequest/delegate.md)
  A delegate that the session request instance informs about authentication completion.
- [protocol ASWebAuthenticationSessionRequestDelegate](./aswebauthenticationsessionrequestdelegate.md)
  An interface through which the session request can inform its delegate, which is typically a browser, about the outcome of the authentication attempt.
### Deprecated symbols
- [var callbackURLScheme: String?](./aswebauthenticationsessionrequest/callbackurlscheme.md)
  The scheme for the browser to use when returning the result of the authentication attempt to the app requesting it.
### Initializers
- [init?(coder: NSCoder)](./aswebauthenticationsessionrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Starting and Stopping a Session Request
- [func begin(ASWebAuthenticationSessionRequest!)](./aswebauthenticationsessionwebbrowsersessionhandling/begin%28_%29.md)
  Handles the given session request from an app.
- [func cancel(ASWebAuthenticationSessionRequest!)](./aswebauthenticationsessionwebbrowsersessionhandling/cancel%28_%29.md)
  Cancels the process of handling the given request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest)*