# AVCustomRoutingControllerDelegate

**Framework**: AVRouting  
**Kind**: protocol  
**Role**: Protocol

A protocol for delegates of a custom routing controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVCustomRoutingControllerDelegate : NSObjectProtocol, Sendable
```

```objc
@protocol AVCustomRoutingControllerDelegate <NSObject>
```

## Topics

### Handling controller events
- [func customRoutingController(AVCustomRoutingController, handle: AVCustomRoutingEvent, completionHandler: (Bool) -> Void)](./avcustomroutingcontrollerdelegate/customroutingcontroller%28_,handle,completionhandler%29.md)
  Connects to, or disconnects from, a device when a user requests it in the picker.
- [func customRoutingController(AVCustomRoutingController, eventDidTimeOut: AVCustomRoutingEvent)](./avcustomroutingcontrollerdelegate/customroutingcontroller%28_,eventdidtimeout%29.md)
  Tells the delegate when a routing event times out.
- [func customRoutingController(AVCustomRoutingController, didSelect: AVCustomRoutingActionItem)](./avcustomroutingcontrollerdelegate/customroutingcontroller%28_,didselect%29.md)
  Tells the delegate when a user selects a custom item in the route picker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media routing
- [class AVCustomRoutingController](./avcustomroutingcontroller.md)
  An object that manages the connection from a device to a destination.
- [class AVCustomRoutingEvent](./avcustomroutingevent.md)
  An object that represents an event that occurs on a route.
- [class AVCustomRoutingActionItem](./avcustomroutingactionitem.md)
  An object that represents a custom action item to display in a device route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontrollerdelegate)*