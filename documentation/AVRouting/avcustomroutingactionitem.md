# AVCustomRoutingActionItem

**Framework**: AVRouting  
**Kind**: class

An object that represents a custom action item to display in a device route picker.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVCustomRoutingActionItem
```

#### Overview

Use this class to specify supplemental action items to display in the list of discovered routes. Tapping a custom item dismisses the picker and calls the [`customRoutingController(_:didSelect:)`](avcustomroutingcontrollerdelegate/customroutingcontroller(_:didselect:).md) method of [`AVCustomRoutingControllerDelegate`](avcustomroutingcontrollerdelegate.md).

## Topics

### Configuring an item
- [var type: UTType](avcustomroutingactionitem/type.md)
  A type with an identifier that matches a value in the app’s configuration.
- [var overrideTitle: String?](avcustomroutingactionitem/overridetitle.md)
  A string to use to override the title of the item’s type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCustomRoutingController](avcustomroutingcontroller.md)
  An object that manages the connection from a device to a destination.
- [protocol AVCustomRoutingControllerDelegate](avcustomroutingcontrollerdelegate.md)
  A protocol for delegates of a custom routing controller.
- [class AVCustomRoutingEvent](avcustomroutingevent.md)
  An object that represents an event that occurs on a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingactionitem)*