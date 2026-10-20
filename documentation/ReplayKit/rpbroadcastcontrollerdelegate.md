# RPBroadcastControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol  
**Role**: Protocol

The protocol you implement to respond to changes in a live broadcast.

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
protocol RPBroadcastControllerDelegate : NSObjectProtocol
```

```objc
@protocol RPBroadcastControllerDelegate <NSObject>
```

## Topics

### Finishing a Broadcast
- [func broadcastController(RPBroadcastController, didFinishWithError: (any Error)?)](./rpbroadcastcontrollerdelegate/broadcastcontroller%28_,didfinishwitherror%29.md)
  Tells the delegate that a broadcast ended due to an error.
### Updating a Broadcast
- [func broadcastController(RPBroadcastController, didUpdateServiceInfo: [String : any NSCoding & NSObjectProtocol])](./rpbroadcastcontrollerdelegate/broadcastcontroller%28_,didupdateserviceinfo%29.md)
  Tells the delegate the broadcast service has data to pass back to the broadcasting app.
- [func broadcastController(RPBroadcastController, didUpdateBroadcast: URL)](./rpbroadcastcontrollerdelegate/broadcastcontroller%28_,didupdatebroadcast%29.md)
  Tells the broadcast service the broadcast URL has been updated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the Delegate
- [var delegate: (any RPBroadcastControllerDelegate)?](./rpbroadcastcontroller/delegate.md)
  The delegate for the broadcast controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate)*