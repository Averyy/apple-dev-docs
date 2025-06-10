# urlSession(_:readClosedFor:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the read side of the underlying socket has been closed.

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
optional func urlSession(_ session: URLSession, readClosedFor streamTask: URLSessionStreamTask)
```

#### Discussion

This method may be called even if no reads are currently in progress. This method does not indicate that the stream reached end-of-file (EOF), such that no more data can be read.

## Parameters

- `session`: The session containing the stream task that closed reads.
- `streamTask`: The stream task that closed reads.

## See Also

- [func urlSession(URLSession, writeClosedFor: URLSessionStreamTask)](urlsessionstreamdelegate/urlsession(_:writeclosedfor:).md)
  Tells the delegate that the write side of the underlying socket has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:readclosedfor:))*