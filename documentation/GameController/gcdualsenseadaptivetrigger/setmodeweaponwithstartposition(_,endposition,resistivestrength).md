# setModeWeaponWithStartPosition(_:endPosition:resistiveStrength:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Sets the mode to provide feedback when the user depresses the trigger between the start and the end positions.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setModeWeaponWithStartPosition(_ startPosition: Float, endPosition: Float, resistiveStrength: Float)
```

```objc
- (void) setModeWeaponWithStartPosition:(float) startPosition endPosition:(float) endPosition resistiveStrength:(float) resistiveStrength;
```

#### Discussion

When the user depresses the trigger beyond the value of the end position, it stops providing feedback, giving the user a sense of release, similar to pulling a weapon trigger.

## Parameters

- `startPosition`: The effect’s start position. A value between `0` and `1` , where `0` is the minimum and `1` is the maximum trigger depression.
- `endPosition`: The effect’s end position. A value between `0` and `1` , where `0` is the minimum and `1` is the maximum trigger depression. This value must be greater than `startPosition`.
- `resistiveStrength`: The strength of the effect. A value between `0` and `1`, where `0` is the minimum or off value, and `1` is the maximum strength.

## See Also

### Configuring the trigger
- [func setModeFeedbackWithStartPosition(Float, resistiveStrength: Float)](./setmodefeedbackwithstartposition%28_,resistivestrength%29.md)
  Sets the mode to provide feedback when the user depresses the trigger at the start position or at a greater value.
- [GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths](./positionalresistivestrengths.md)
  The resistive strengths for multiple positions on a trigger.
- [func setModeFeedback(resistiveStrengths: GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths)](./setmodefeedback%28resistivestrengths%29.md)
  Sets the mode to provide feedback with the specified strengths for each possible trigger position.
- [func setModeVibrationWithStartPosition(Float, amplitude: Float, frequency: Float)](./setmodevibrationwithstartposition%28_,amplitude,frequency%29.md)
  Sets the mode to vibrate when the user depresses the trigger at the start position or at a greater value.
- [func setModeVibration(amplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)](./setmodevibration%28amplitudes,frequency%29.md)
  Sets the mode to vibrate with the specified amplitudes for each possible trigger position.
- [GCDualSenseAdaptiveTrigger.PositionalAmplitudes](./positionalamplitudes.md)
  The amplitudes for multiple positions on a trigger.
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](./setmodeslopefeedback%28startposition,endposition,startstrength,endstrength%29.md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/setmodeweaponwithstartposition(_:endposition:resistivestrength:))*