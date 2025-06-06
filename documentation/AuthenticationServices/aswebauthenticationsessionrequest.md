# ASWebAuthenticationSessionRequest

**Framework**: Authentication Services  
**Kind**: class

A login session request that a web browser receives from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class ASWebAuthenticationSessionRequest
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

## Topics

### Interpreting a Request
- [var url: URL](aswebauthenticationsessionrequest/url.md)
  The web address the browser should use to perform the authentication request.
- [var callbackURLScheme: String?](aswebauthenticationsessionrequest/callbackurlscheme.md)
  The scheme the browser should use to return the result of the authentication attempt to the app requesting it.
- [var shouldUseEphemeralSession: Bool](aswebauthenticationsessionrequest/shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var uuid: UUID](aswebauthenticationsessionrequest/uuid.md)
  A unique identifier for the request.
### Finishing a Request
- [func complete(withCallbackURL: URL)](aswebauthenticationsessionrequest/complete(withcallbackurl:).md)
  Indicates that the browser successfully completed the authentication attempt.
- [func cancelWithError(any Error)](aswebauthenticationsessionrequest/cancelwitherror(_:).md)
  Indicates that the browser canceled the authentication attempt.
### Indicating Completion
- [var delegate: (any ASWebAuthenticationSessionRequestDelegate)?](aswebauthenticationsessionrequest/delegate.md)
  A delegate that the session request instance informs about authentication completion.
- [protocol ASWebAuthenticationSessionRequestDelegate](aswebauthenticationsessionrequestdelegate.md)
  An interface through which the session request can inform its delegate, which is typically a browser, about the outcome of the authentication attempt.
### Instance Properties
- [var additionalHeaderFields: [String : String]?](aswebauthenticationsessionrequest/additionalheaderfields.md)
- [var callback: ASWebAuthenticationSession.Callback?](aswebauthenticationsessionrequest/callback.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func begin(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/begin(_:).md)
  Handles the given session request from an app.
- [func cancel(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/cancel(_:).md)
  Cancels the process of handling the given request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest)*