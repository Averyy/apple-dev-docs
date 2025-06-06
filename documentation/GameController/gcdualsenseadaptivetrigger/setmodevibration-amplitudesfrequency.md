# setModeVibration(amplitudes:frequency:)

**Framework**: Game Controller  
**Kind**: method

Sets the mode to vibrate with the specified amplitudes for each possible trigger position.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func setModeVibration(amplitudes positionalAmplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)
```

## Parameters

- `positionalAmplitudes`: The amplitudes for each possible trigger position.
- `frequency`: The frequency of the vibration effect, which is a value between   and  , where   is the minimum and   is the maximum frequency.

## See Also

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
- [GCDualSenseAdaptiveTrigger.PositionalAmplitudes](gcdualsenseadaptivetrigger/positionalamplitudes.md)
  The amplitudes for multiple positions on a trigger.
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](gcdualsenseadaptivetrigger/setmodeslopefeedback(startposition:endposition:startstrength:endstrength:).md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/setmodevibration(amplitudes:frequency:))*