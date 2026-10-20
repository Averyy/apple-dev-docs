# startBroadcast(handler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Starts a broadcast.

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
func startBroadcast(handler: @escaping ((any Error)?) -> Void)
```

```objc
- (void) startBroadcastWithHandler:(void (^)(NSError *error)) handler;
```

## Parameters

- `handler`: A block that is called after a broadcast has started.

  - **`error`**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](../rprecordingerrorcode.md) for a list of error codes specific to ReplayKit.

## See Also

### Controlling the Broadcast
- [var broadcastURL: URL](./broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func pauseBroadcast()](./pausebroadcast%28%29.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](./resumebroadcast%28%29.md)
  Resumes a paused broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](./finishbroadcast%28handler%29.md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](./serviceinfo.md)
  Information updated by the service during a broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/startbroadcast(handler:))*