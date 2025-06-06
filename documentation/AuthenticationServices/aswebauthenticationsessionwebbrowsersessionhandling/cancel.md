# cancel(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Cancels the process of handling the given request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func cancel(_ request: ASWebAuthenticationSessionRequest!)
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Discussion

Your browser app implements this method to accept cancellation requests from the initiating app.

When you’ve finished your app’s teardown activities in your implementation of this method, call [`cancelWithError(_:)`](aswebauthenticationsessionrequest/cancelwitherror(_:).md) on the provided request object. Use [`ASWebAuthenticationSessionErrorDomain`](aswebauthenticationsessionerrordomain.md) for the error domain and [`ASWebAuthenticationSessionError.Code.canceledLogin`](aswebauthenticationsessionerror/code/canceledlogin.md) for the error code, unless another error happened that you need to communicate to the system.

## Parameters

- `request`: The request to cancel.

## See Also

- [func begin(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/begin(_:).md)
  Handles the given session request from an app.
- [class ASWebAuthenticationSessionRequest](aswebauthenticationsessionrequest.md)
  A login session request that a web browser receives from an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionhandling/cancel(_:))*