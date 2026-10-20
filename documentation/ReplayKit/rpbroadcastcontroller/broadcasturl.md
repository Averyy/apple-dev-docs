# broadcastURL

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A URL that redirects users to an ongoing or completed broadcast.

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
var broadcastURL: URL { get }
```

```objc
@property (nonatomic, readonly) NSURL * broadcastURL;
```

## See Also

### Controlling the Broadcast
- [func startBroadcast(handler: ((any Error)?) -> Void)](./startbroadcast%28handler%29.md)
  Starts a broadcast.
- [func pauseBroadcast()](./pausebroadcast%28%29.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](./resumebroadcast%28%29.md)
  Resumes a paused broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](./finishbroadcast%28handler%29.md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](./serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/broadcasturl)*