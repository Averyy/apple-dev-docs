# setModeSlopeFeedback(startPosition:endPosition:startStrength:endStrength:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)
```

```objc
- (void) setModeSlopeFeedbackWithStartPosition:(float) startPosition endPosition:(float) endPosition startStrength:(float) startStrength endStrength:(float) endStrength;
```

## Parameters

- `startPosition`: The effect’s start position, which is a value between `0` and `1` , where `0` is the minimum and `1` is the maximum trigger tilt.
- `endPosition`: The effect’s end position, which is a value between `0` and `1` , where `0` is the minimum and `1` is the maximum trigger tilt. This value must be greater than `startPosition`.
- `startStrength`: The effect’s start strength, which is a value between `0` and `1`, where `0` is the minimum or off value, and `1` is the maximum strength.
- `endStrength`: The effect’s end strength, which is a value between `0` and `1`, where `0` is the minimum or off value, and `1` is the maximum strength.

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
- [func setModeVibrationWithStartPosition(Float, amplitude: Float, frequency: Float)](./setmodevibrationwithstartposition%28_,amplitude,frequency%29.md)
  Sets the mode to vibrate when the user depresses the trigger at the start position or at a greater value.
- [func setModeVibration(amplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)](./setmodevibration%28amplitudes,frequency%29.md)
  Sets the mode to vibrate with the specified amplitudes for each possible trigger position.
- [GCDualSenseAdaptiveTrigger.PositionalAmplitudes](./positionalamplitudes.md)
  The amplitudes for multiple positions on a trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/setmodeslopefeedback(startposition:endposition:startstrength:endstrength:))*