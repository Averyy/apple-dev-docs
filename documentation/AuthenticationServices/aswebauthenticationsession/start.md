# start()

**Framework**: Authentication Services  
**Kind**: method

Starts a web authentication session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func start() -> Bool
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)
- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Return Value

A Boolean value indicating whether the web authentication session started successfully.

#### Discussion

Only call this method once for a given [`ASWebAuthenticationSession`](aswebauthenticationsession.md) instance after initialization. Calling the [`start()`](aswebauthenticationsession/start().md) method on a canceled session results in a failure.

In macOS, and for iOS apps with a deployment target of iOS 13 or later, after you call [`start()`](aswebauthenticationsession/start().md), the session instance stores a strong reference to itself. To avoid deallocation during the authentication process, the session keeps the reference until after it calls the completion handler.

For iOS apps with a deployment target earlier than iOS 13, your app must keep a strong reference to the session to prevent the system from deallocating the session while waiting for authentication to complete.

## See Also

- [var canStart: Bool](aswebauthenticationsession/canstart.md)
  A Boolean indicating whether the session can begin.
- [func cancel()](aswebauthenticationsession/cancel.md)
  Cancels a web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/start())*