# broadcastController(_:didUpdateServiceInfo:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the broadcast service has data to pass back to the broadcasting app.

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
optional func broadcastController(_ broadcastController: RPBroadcastController, didUpdateServiceInfo serviceInfo: [String : any NSCoding & NSObjectProtocol])
```

```objc
- (void) broadcastController:(RPBroadcastController *) broadcastController didUpdateServiceInfo:(NSDictionary<NSString *,NSObject<NSCoding> *> *) serviceInfo;
```

## Parameters

- `broadcastController`: The RPBroadcastController instance.
- `serviceInfo`: Dictionary that is passed back to the broadcasting app and contains information about the ongoing broadcast.

## See Also

### Updating a Broadcast
- [func broadcastController(RPBroadcastController, didUpdateBroadcast: URL)](./broadcastcontroller%28_,didupdatebroadcast%29.md)
  Tells the broadcast service the broadcast URL has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdateserviceinfo:))*