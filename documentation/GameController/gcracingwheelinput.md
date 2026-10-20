# GCRacingWheelInput

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A controller profile that supports a racing wheel.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class GCRacingWheelInput
```

```objc
@interface GCRacingWheelInput : GCRacingWheelInputState
```

## Mentions

- [Handling input events](./handling-input-events.md)

## Topics

### Creating snapshots
- [func capture() -> GCRacingWheelInputState](./gcracingwheelinput/capture%28%29.md)
  Returns a snapshot of the racing wheel inputs.
### Polling for input
- [func nextInputState() -> (any GCRacingWheelInputState & GCDevicePhysicalInputStateDiff)?](./gcracingwheelinput/nextinputstate%28%29.md)
  Returns the next input state of the racing wheel from the queue.

## Relationships

### Inherits From
- [GCRacingWheelInputState](./gcracingwheelinputstate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GCDevicePhysicalInput](./gcdevicephysicalinput.md)
- [GCDevicePhysicalInputState](./gcdevicephysicalinputstate.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Racing wheel input
- [class GCRacingWheelInputState](./gcracingwheelinputstate.md)
  The input for the wheel of a racing wheel controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinput)*