# accessLog()

**Framework**: AVFoundation  
**Kind**: method

Returns an object that represents a snapshot of the network access log.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func accessLog() -> AVPlayerItemAccessLog?
```

#### Return Value

An object that represents a snapshot of the network access log. The returned value can be `nil`.

#### Discussion

If the method returns `nil`, there is no logging information currently available for the player item.

## See Also

- [class AVPlayerItemAccessLog](avplayeritemaccesslog.md)
  An object used to retrieve the access log associated with a player item.
- [class AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](avplayeritemerrorlog.md)
  The error log associated with a player item.
- [class AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/accesslog())*