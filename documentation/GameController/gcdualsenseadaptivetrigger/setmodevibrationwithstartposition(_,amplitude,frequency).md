# setModeVibrationWithStartPosition(_:amplitude:frequency:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Sets the mode to vibrate when the user depresses the trigger at the start position or at a greater value.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setModeVibrationWithStartPosition(_ startPosition: Float, amplitude: Float, frequency: Float)
```

```objc
- (void) setModeVibrationWithStartPosition:(float) startPosition amplitude:(float) amplitude frequency:(float) frequency;
```

## Parameters

- `startPosition`: The effect’s start position. A value between `0` and `1` , where `0` is the minimum and `1` is the maximum trigger depression.
- `amplitude`: The amplitude of the vibration effect. A value between `0` and `1`, where `0` is the minimum and `1` is the maximum amplitude.
- `frequency`: The frequency of the vibration effect, which is a value between `0` and `1`, where `0` is the minimum and `1` is the maximum frequency.

## See Also

### Configuring the trigger
- [func setModeFeedbackWithStartPosition(Float, resistiveStrength: Float)](./setmodefeedbackwithstartposition%28_,resistivestrength%29.md)
  Sets the mode to provide feedback when the user depresses the trigger at the start position or at a greater value.
- [GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths](./positionalresistivestrengths.md)
  The resistive strengths for multiple positions on a trigger.
- [func setModeFeedback(resistiveStrengths: GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths)](./setmodefeedback%28resistivestrengths%29.md)
  Sets the mode to provide feedback with the specified strengths for each possible trigger position.
- [func setModeWeaponWithStartPosition(Float, endPosition: Float, resistiveStrength: Float)](./setmodeweaponwithstartposition%28_,endposition,resistivestrength%29.md)
  Sets the mode to provide feedback when the user depresses the trigger between the start and the end positions.
- [func setModeVibration(amplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)](./setmodevibration%28amplitudes,frequency%29.md)
  Sets the mode to vibrate with the specified amplitudes for each possible trigger position.
- [GCDualSenseAdaptiveTrigger.PositionalAmplitudes](./positionalamplitudes.md)
  The amplitudes for multiple positions on a trigger.
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](./setmodeslopefeedback%28startposition,endposition,startstrength,endstrength%29.md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/setmodevibrationwithstartposition(_:amplitude:frequency:))*