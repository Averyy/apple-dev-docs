# GCRacingWheelInput

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports a racing wheel.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class GCRacingWheelInput
```

## Mentions

- [Handling input events](handling-input-events.md)

## Topics

### Creating snapshots
- [func capture() -> GCRacingWheelInputState](gcracingwheelinput/capture.md)
  Returns a snapshot of the racing wheel inputs.
### Polling for input
- [func nextInputState() -> (any GCRacingWheelInputState & GCDevicePhysicalInputStateDiff)?](gcracingwheelinput/nextinputstate.md)
  Returns the next input state of the racing wheel from the queue.

## Relationships

### Inherits From
- [GCRacingWheelInputState](gcracingwheelinputstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GCDevicePhysicalInput](gcdevicephysicalinput.md)
- [GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCRacingWheelInputState](gcracingwheelinputstate.md)
  The input for the wheel of a racing wheel controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinput)*