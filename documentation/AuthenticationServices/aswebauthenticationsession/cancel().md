# cancel()

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancel;
```

## Mentions

- [Authenticating a User Through a Web Service](../authenticating-a-user-through-a-web-service.md)

## Discussion

If the session has already presented a view with the authentication webpage, calling this method dismisses that view. Calling [`cancel()`](./cancel%28%29.md) on an already canceled session has no effect.

## See Also

### Starting and Stopping a Session
- [var canStart: Bool](./canstart.md)
  A Boolean indicating whether the session can begin.
- [func start() -> Bool](./start%28%29.md)
  Starts a web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/cancel())*