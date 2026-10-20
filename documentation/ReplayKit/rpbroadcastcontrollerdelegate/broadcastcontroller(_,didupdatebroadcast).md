# broadcastController(_:didUpdateBroadcast:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Tells the broadcast service the broadcast URL has been updated.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func broadcastController(_ broadcastController: RPBroadcastController, didUpdateBroadcast broadcastURL: URL)
```

```objc
- (void) broadcastController:(RPBroadcastController *) broadcastController didUpdateBroadcastURL:(NSURL *) broadcastURL;
```

## Parameters

- `broadcastController`: The broadcast controller instance.
- `broadcastURL`: The URL of the resource where the broadcast can be viewed.

## See Also

### Updating a Broadcast
- [func broadcastController(RPBroadcastController, didUpdateServiceInfo: [String : any NSCoding & NSObjectProtocol])](./broadcastcontroller%28_,didupdateserviceinfo%29.md)
  Tells the delegate the broadcast service has data to pass back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdatebroadcast:))*