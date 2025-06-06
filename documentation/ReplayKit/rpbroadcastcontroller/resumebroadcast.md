# resumeBroadcast()

**Framework**: ReplayKit  
**Kind**: method

Resumes a paused broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func resumeBroadcast()
```

## See Also

- [var broadcastURL: URL](rpbroadcastcontroller/broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func startBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/startbroadcast(handler:).md)
  Starts a broadcast.
- [func pauseBroadcast()](rpbroadcastcontroller/pausebroadcast.md)
  Pauses the current broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/finishbroadcast(handler:).md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](rpbroadcastcontroller/serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/resumebroadcast())*