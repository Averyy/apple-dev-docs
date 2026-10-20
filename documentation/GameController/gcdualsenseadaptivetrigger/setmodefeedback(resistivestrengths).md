# setModeFeedback(resistiveStrengths:)

**Framework**: Game Controller  
**Kind**: method

Sets the mode to provide feedback with the specified strengths for each possible trigger position.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func setModeFeedback(resistiveStrengths positionalResistiveStrengths: GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths)
```

## Parameters

- `positionalResistiveStrengths`: The resistance values for each possible trigger position.

## See Also

- [func setModeFeedbackWithStartPosition(Float, resistiveStrength: Float)](gcdualsenseadaptivetrigger/setmodefeedbackwithstartposition(_:resistivestrength:).md)
  Sets the mode to provide feedback when the user depresses the trigger at the start position or at a greater value.
- [GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths](gcdualsenseadaptivetrigger/positionalresistivestrengths.md)
  The resistive strengths for multiple positions on a trigger.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/setmodefeedback(resistivestrengths:))*