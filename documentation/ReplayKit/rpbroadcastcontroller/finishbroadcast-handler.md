# finishBroadcast(handler:)

**Framework**: ReplayKit  
**Kind**: method

Stops the current broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func finishBroadcast(handler: @escaping ((any Error)?) -> Void)
```

#### Discussion

Use this method when the user is finished with a broadcast. To temporarily pause a broadcast, use [`pauseBroadcast()`](rpbroadcastcontroller/pausebroadcast().md).

## Parameters

- `handler`: A block that is called after the broadcast has finished.

## See Also

- [var broadcastURL: URL](rpbroadcastcontroller/broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func startBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/startbroadcast(handler:).md)
  Starts a broadcast.
- [func pauseBroadcast()](rpbroadcastcontroller/pausebroadcast.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](rpbroadcastcontroller/resumebroadcast.md)
  Resumes a paused broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](rpbroadcastcontroller/serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/finishbroadcast(handler:))*