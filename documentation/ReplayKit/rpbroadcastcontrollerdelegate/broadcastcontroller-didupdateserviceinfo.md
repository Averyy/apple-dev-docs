# broadcastController(_:didUpdateServiceInfo:)

**Framework**: ReplayKit  
**Kind**: method

Tells the delegate the broadcast service has data to pass back to the broadcasting app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func broadcastController(_ broadcastController: RPBroadcastController, didUpdateServiceInfo serviceInfo: [String : any NSCoding & NSObjectProtocol])
```

## Parameters

- `broadcastController`: The RPBroadcastController instance.
- `serviceInfo`: Dictionary that is passed back to the broadcasting app and contains information about the ongoing broadcast.

## See Also

- [func broadcastController(RPBroadcastController, didUpdateBroadcast: URL)](rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdatebroadcast:).md)
  Tells the broadcast service the broadcast URL has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdateserviceinfo:))*