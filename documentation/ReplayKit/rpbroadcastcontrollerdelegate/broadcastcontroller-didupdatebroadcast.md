# broadcastController(_:didUpdateBroadcast:)

**Framework**: ReplayKit  
**Kind**: method

Tells the broadcast service the broadcast URL has been updated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func broadcastController(_ broadcastController: RPBroadcastController, didUpdateBroadcast broadcastURL: URL)
```

## Parameters

- `broadcastController`: The broadcast controller instance.
- `broadcastURL`: The URL of the resource where the broadcast can be viewed.

## See Also

- [func broadcastController(RPBroadcastController, didUpdateServiceInfo: [String : any NSCoding & NSObjectProtocol])](rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdateserviceinfo:).md)
  Tells the delegate the broadcast service has data to pass back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdatebroadcast:))*