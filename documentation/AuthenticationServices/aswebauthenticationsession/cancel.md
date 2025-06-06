# cancel()

**Framework**: Authentication Services  
**Kind**: method

Cancels a web authentication session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func cancel()
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)

#### Discussion

If the session has already presented a view with the authentication webpage, calling this method dismisses that view. Calling [`cancel()`](aswebauthenticationsession/cancel().md) on an already canceled session has no effect.

## See Also

- [var canStart: Bool](aswebauthenticationsession/canstart.md)
  A Boolean indicating whether the session can begin.
- [func start() -> Bool](aswebauthenticationsession/start.md)
  Starts a web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/cancel())*