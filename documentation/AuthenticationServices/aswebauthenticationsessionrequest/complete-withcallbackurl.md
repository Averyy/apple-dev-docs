# complete(withCallbackURL:)

**Framework**: Authentication Services  
**Kind**: method

Indicates that the browser successfully completed the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func complete(withCallbackURL url: URL)
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Discussion

Call this method from your browser app when the authentication attempt completes to report the result of the attempt using the callback URL.

## Parameters

- `url`: A URL using the scheme indicated by the request’s   property that indicates the outcome of the authentication attempt.

## See Also

- [func cancelWithError(any Error)](aswebauthenticationsessionrequest/cancelwitherror(_:).md)
  Indicates that the browser canceled the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/complete(withcallbackurl:))*