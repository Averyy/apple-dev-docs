# resumeBroadcast()

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Resumes a paused broadcast.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func resumeBroadcast()
```

```objc
- (void) resumeBroadcast;
```

## See Also

### Controlling the Broadcast
- [var broadcastURL: URL](./broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func startBroadcast(handler: ((any Error)?) -> Void)](./startbroadcast%28handler%29.md)
  Starts a broadcast.
- [func pauseBroadcast()](./pausebroadcast%28%29.md)
  Pauses the current broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](./finishbroadcast%28handler%29.md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](./serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/resumebroadcast())*