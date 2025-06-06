# customRoutingController(_:eventDidTimeOut:)

**Framework**: AVRouting  
**Kind**: method

Tells the delegate when a routing event times out.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func customRoutingController(_ controller: AVCustomRoutingController, eventDidTimeOut event: AVCustomRoutingEvent)
```

#### Discussion

Adopt this method to clean up any in-progress connection attempts.

## Parameters

- `controller`: A custom routing controller.
- `event`: An event that times out.

## See Also

- [func customRoutingController(AVCustomRoutingController, handle: AVCustomRoutingEvent, completionHandler: (Bool) -> Void)](avcustomroutingcontrollerdelegate/customroutingcontroller(_:handle:completionhandler:).md)
  Connects to, or disconnects from, a device when a user requests it in the picker.
- [func customRoutingController(AVCustomRoutingController, didSelect: AVCustomRoutingActionItem)](avcustomroutingcontrollerdelegate/customroutingcontroller(_:didselect:).md)
  Tells the delegate when a user selects a custom item in the route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontrollerdelegate/customroutingcontroller(_:eventdidtimeout:))*