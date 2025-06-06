# broadcastURL

**Framework**: ReplayKit  
**Kind**: property

A URL that redirects users to an ongoing or completed broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var broadcastURL: URL { get }
```

## See Also

- [func startBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/startbroadcast(handler:).md)
  Starts a broadcast.
- [func pauseBroadcast()](rpbroadcastcontroller/pausebroadcast.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](rpbroadcastcontroller/resumebroadcast.md)
  Resumes a paused broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/finishbroadcast(handler:).md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](rpbroadcastcontroller/serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/broadcasturl)*