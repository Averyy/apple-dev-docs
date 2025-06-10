# urlSession(_:didBecomeInvalidWithError:)

**Framework**: Foundation  
**Kind**: method

Tells the URL session that the session has been invalidated.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, didBecomeInvalidWithError error: (any Error)?)
```

#### Discussion

If you invalidate a session by calling its [`finishTasksAndInvalidate()`](urlsession/finishtasksandinvalidate().md) method, the session waits until after the final task in the session finishes or fails before calling this delegate method. If you call the [`invalidateAndCancel()`](urlsession/invalidateandcancel().md) method, the session calls this delegate method immediately.

## Parameters

- `session`: The session object that was invalidated.
- `error`: The error that caused invalidation, or   if the invalidation was explicit.

## See Also

- [func urlSessionDidFinishEvents(forBackgroundURLSession: URLSession)](urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:).md)
  Tells the delegate that all messages enqueued for a session have been delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsession(_:didbecomeinvalidwitherror:))*