# serviceInfo

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

Information updated by the service during a broadcast.

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
var serviceInfo: [String : any NSCoding & NSObjectProtocol]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSObject<NSCoding> *> * serviceInfo;
```

## Discussion

The keys and values for the dictionary are defined by the broadcast service and updated through the [`updateServiceInfo(_:)`](../rpbroadcasthandler/updateserviceinfo%28_%29.md) function. This property is KVO observable.

## See Also

### Controlling the Broadcast
- [var broadcastURL: URL](./broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func startBroadcast(handler: ((any Error)?) -> Void)](./startbroadcast%28handler%29.md)
  Starts a broadcast.
- [func pauseBroadcast()](./pausebroadcast%28%29.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](./resumebroadcast%28%29.md)
  Resumes a paused broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](./finishbroadcast%28handler%29.md)
  Stops the current broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/serviceinfo)*