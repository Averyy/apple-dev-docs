# DockAccessory.StateChange

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

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

DockKit generates this event when a device docks or undocks from the dock accessory, or when a person presses the tracking button. To iterate the stream of state changes, see [`accessoryStateChanges`](../dockaccessorymanager/accessorystatechanges.md).

## Topics

### Getting properties
- [let accessory: DockAccessory?](./statechange/accessory.md)
  The dock accessory that generated the event.
- [let state: DockAccessory.State](./statechange/state.md)
  The state of the dock accessory associated with the event.
### Instance Properties
- [let trackingButtonEnabled: Bool](./statechange/trackingbuttonenabled.md)
  The state of the tracking button on the dock accessory.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting accessory information
- [var firmwareVersion: String?](./firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](./hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](./identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](./identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](./category.md)
  Types of supported dock accesories.
- [DockAccessory.State](./state.md)
  The state of a dock accessory.
- [DockAccessory.StateChanges](./statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/statechange)*