# customRoutingController(_:didSelect:)

**Framework**: AVRouting  
**Kind**: method

Tells the delegate when a user selects a custom item in the route picker.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func customRoutingController(_ controller: AVCustomRoutingController, didSelect customActionItem: AVCustomRoutingActionItem)
```

## Parameters

- `controller`: A custom routing controller.
- `customActionItem`: The selected action item.

## See Also

- [func customRoutingController(AVCustomRoutingController, handle: AVCustomRoutingEvent, completionHandler: (Bool) -> Void)](avcustomroutingcontrollerdelegate/customroutingcontroller(_:handle:completionhandler:).md)
  Connects to, or disconnects from, a device when a user requests it in the picker.
- [func customRoutingController(AVCustomRoutingController, eventDidTimeOut: AVCustomRoutingEvent)](avcustomroutingcontrollerdelegate/customroutingcontroller(_:eventdidtimeout:).md)
  Tells the delegate when a routing event times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontrollerdelegate/customroutingcontroller(_:didselect:))*