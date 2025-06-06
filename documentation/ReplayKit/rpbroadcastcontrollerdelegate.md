# RPBroadcastControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol

The protocol you implement to respond to changes in a live broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol RPBroadcastControllerDelegate : NSObjectProtocol
```

## Topics

### Finishing a Broadcast
- [func broadcastController(RPBroadcastController, didFinishWithError: (any Error)?)](rpbroadcastcontrollerdelegate/broadcastcontroller(_:didfinishwitherror:).md)
  Tells the delegate that a broadcast ended due to an error.
### Updating a Broadcast
- [func broadcastController(RPBroadcastController, didUpdateServiceInfo: [String : any NSCoding & NSObjectProtocol])](rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdateserviceinfo:).md)
  Tells the delegate the broadcast service has data to pass back to the broadcasting app.
- [func broadcastController(RPBroadcastController, didUpdateBroadcast: URL)](rpbroadcastcontrollerdelegate/broadcastcontroller(_:didupdatebroadcast:).md)
  Tells the broadcast service the broadcast URL has been updated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any RPBroadcastControllerDelegate)?](rpbroadcastcontroller/delegate.md)
  The delegate for the broadcast controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate)*