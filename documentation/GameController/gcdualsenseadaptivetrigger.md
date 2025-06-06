# GCDualSenseAdaptiveTrigger

**Framework**: Game Controller  
**Kind**: class

A class that encapsulates the features of a DualSense adaptive trigger.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
class GCDualSenseAdaptiveTrigger
```

#### Overview

A `GCDualSenseAdaptiveTrigger` object allows you to specify a dynamic resistance force that the DualSense controller applies when the user pulls the trigger. For example, set the resistance to give the user the feeling of pulling back on a bow string, firing a weapon, or pulling a lever.

## Topics

### Getting the mode
- [var mode: GCDualSenseAdaptiveTrigger.Mode](gcdualsenseadaptivetrigger/mode-swift.property.md)
  The current configuration of the adaptive trigger.
- [GCDualSenseAdaptiveTrigger.Mode](gcdualsenseadaptivetrigger/mode-swift.enum.md)
  The possible modes of an adaptive trigger.
- [func setModeOff()](gcdualsenseadaptivetrigger/setmodeoff.md)
  Sets the mode to off and stops any trigger effect.
### Configuring the trigger
- [func setModeFeedbackWithStartPosition(Float, resistiveStrength: Float)](gcdualsenseadaptivetrigger/setmodefeedbackwithstartposition(_:resistivestrength:).md)
  Sets the mode to provide feedback when the user depresses the trigger at the start position or at a greater value.
- [GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths](gcdualsenseadaptivetrigger/positionalresistivestrengths.md)
  The resistive strengths for multiple positions on a trigger.
- [func setModeFeedback(resistiveStrengths: GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths)](gcdualsenseadaptivetrigger/setmodefeedback(resistivestrengths:).md)
  Sets the mode to provide feedback with the specified strengths for each possible trigger position.
- [func setModeWeaponWithStartPosition(Float, endPosition: Float, resistiveStrength: Float)](gcdualsenseadaptivetrigger/setmodeweaponwithstartposition(_:endposition:resistivestrength:).md)
  Sets the mode to provide feedback when the user depresses the trigger between the start and the end positions.
- [func setModeVibrationWithStartPosition(Float, amplitude: Float, frequency: Float)](gcdualsenseadaptivetrigger/setmodevibrationwithstartposition(_:amplitude:frequency:).md)
  Sets the mode to vibrate when the user depresses the trigger at the start position or at a greater value.
- [func setModeVibration(amplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)](gcdualsenseadaptivetrigger/setmodevibration(amplitudes:frequency:).md)
  Sets the mode to vibrate with the specified amplitudes for each possible trigger position.
- [GCDualSenseAdaptiveTrigger.PositionalAmplitudes](gcdualsenseadaptivetrigger/positionalamplitudes.md)
  The amplitudes for multiple positions on a trigger.
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](gcdualsenseadaptivetrigger/setmodeslopefeedback(startposition:endposition:startstrength:endstrength:).md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.
### Getting the arm position
- [var armPosition: Float](gcdualsenseadaptivetrigger/armposition.md)
  The position of the trigger’s arm.
- [class var discretePositionCount: Int](gcdualsenseadaptivetrigger/discretepositioncount.md)
  The number of discrete control positions that the DualSense adaptive triggers support.
### Checking the status
- [var status: GCDualSenseAdaptiveTrigger.Status](gcdualsenseadaptivetrigger/status-swift.property.md)
  The current status of the adaptive trigger and whether it’s applying effects.
- [GCDualSenseAdaptiveTrigger.Status](gcdualsenseadaptivetrigger/status-swift.enum.md)
  The possible states of an adaptive trigger.

## Relationships

### Inherits From
- [GCControllerButtonInput](gccontrollerbuttoninput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCControllerElement](gccontrollerelement.md)
  An input for a physical control, such as a button or thumbstick.
- [class GCControllerAxisInput](gccontrolleraxisinput.md)
  A control element that tracks movement along an axis.
- [class GCControllerButtonInput](gccontrollerbuttoninput.md)
  A control element that represents a button touch or press.
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger)*