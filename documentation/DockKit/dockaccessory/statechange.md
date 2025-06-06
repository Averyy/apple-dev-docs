# DockAccessory.StateChange

**Framework**: DockKit  
**Kind**: struct

An event that indicates a change in the state of a dock accessory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct StateChange
```

#### Overview

DockKit generates this event when a device docks or undocks from the dock accessory, or when a person presses the tracking button. To iterate the stream of state changes, see [`accessoryStateChanges`](dockaccessorymanager/accessorystatechanges.md).

## Topics

### Getting properties
- [let accessory: DockAccessory?](dockaccessory/statechange/accessory.md)
  The dock accessory that generated the event.
- [let state: DockAccessory.State](dockaccessory/statechange/state.md)
  The state of the dock accessory associated with the event.
### Instance Properties
- [let trackingButtonEnabled: Bool](dockaccessory/statechange/trackingbuttonenabled.md)
  The state of the tracking button on the dock accessory.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var firmwareVersion: String?](dockaccessory/firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](dockaccessory/hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](dockaccessory/identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](dockaccessory/identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](dockaccessory/category.md)
  Types of supported dock accesories.
- [DockAccessory.State](dockaccessory/state.md)
  The state of a dock accessory.
- [DockAccessory.StateChanges](dockaccessory/statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechange)*