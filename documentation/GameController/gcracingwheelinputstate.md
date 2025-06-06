# GCRacingWheelInputState

**Framework**: Game Controller  
**Kind**: class

The input for the wheel of a racing wheel controller.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class GCRacingWheelInputState
```

## Topics

### Getting input elements
- [var wheel: GCSteeringWheelElement](gcracingwheelinputstate/wheel.md)
  The controller’s wheel element.
- [var acceleratorPedal: (any GCButtonElement)?](gcracingwheelinputstate/acceleratorpedal.md)
  The controller’s accelerator pedal element.
- [var brakePedal: (any GCButtonElement)?](gcracingwheelinputstate/brakepedal.md)
  The controller’s brake pedal element.
- [var clutchPedal: (any GCButtonElement)?](gcracingwheelinputstate/clutchpedal.md)
  The controller’s clutch element.
- [var shifter: GCGearShifterElement?](gcracingwheelinputstate/shifter.md)
  The controller’s gear shift element.
### Accessing elements by name
- [var GCInputSteeringWheel: String](gcinputsteeringwheel-26283.md)
  The name of the steering wheel element.
- [var GCInputShifter: String](gcinputshifter-6miga.md)
  The name of the shifter element.
- [var GCInputPedalClutch: String](gcinputpedalclutch-82gwe.md)
  The name of the clutch element.
- [var GCInputPedalAccelerator: String](gcinputpedalaccelerator-6kg6u.md)
  The name of the accelerator element.
- [var GCInputPedalBrake: String](gcinputpedalbrake-6wpdc.md)
  The name of the brake element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GCRacingWheelInput](gcracingwheelinput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCRacingWheelInput](gcracingwheelinput.md)
  A controller profile that supports a racing wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinputstate)*