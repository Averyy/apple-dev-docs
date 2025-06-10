# urlSession(_:writeClosedFor:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the write side of the underlying socket has been closed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, writeClosedFor streamTask: URLSessionStreamTask)
```

#### Discussion

This method may be called even if no writes are currently in progress.

## Parameters

- `session`: The session containing the stream task that closed writes.
- `streamTask`: The stream task that closed writes.

## See Also

- [func urlSession(URLSession, readClosedFor: URLSessionStreamTask)](urlsessionstreamdelegate/urlsession(_:readclosedfor:).md)
  Tells the delegate that the read side of the underlying socket has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:writeclosedfor:))*