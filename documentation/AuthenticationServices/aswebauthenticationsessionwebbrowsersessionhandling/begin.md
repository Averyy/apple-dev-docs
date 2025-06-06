# begin(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Handles the given session request from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func begin(_ request: ASWebAuthenticationSessionRequest!)
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Discussion

Your browser app implements this method to accept requests from apps that want to use single sign-on for authentication. Inspect the given request to see what URL to use for the request, and what call back scheme to use to reply to the app. Call the request’s [`complete(withCallbackURL:)`](aswebauthenticationsessionrequest/complete(withcallbackurl:).md) method to indicate a completed authentication. Call the [`cancelWithError(_:)`](aswebauthenticationsessionrequest/cancelwitherror(_:).md) method if the browser can’t complete the operation, for example because the user cancels it.

## Parameters

- `request`: The request to begin handling.

## See Also

- [func cancel(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/cancel(_:).md)
  Cancels the process of handling the given request.
- [class ASWebAuthenticationSessionRequest](aswebauthenticationsessionrequest.md)
  A login session request that a web browser receives from an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionhandling/begin(_:))*