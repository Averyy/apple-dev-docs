# GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

The resistive strengths for multiple positions on a trigger.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
struct PositionalResistiveStrengths
```

```c
typedef struct { ... } GCDualSenseAdaptiveTriggerPositionalResistiveStrengths;
```

## Topics

### Creating resistive strengths
- [init(values: (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float))](./positionalresistivestrengths/init%28values%29.md)
  Creates a resistive strengths structure with the specified strength values.
- [init()](./positionalresistivestrengths/init%28%29.md)
  Creates an empty resistive strengths structure.
### Accessing resistive strengths
- [var values: (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)](./positionalresistivestrengths/values.md)
  The resistive strength values for possible trigger positions.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Configuring the trigger
- [func setModeFeedbackWithStartPosition(Float, resistiveStrength: Float)](./setmodefeedbackwithstartposition%28_,resistivestrength%29.md)
  Sets the mode to provide feedback when the user depresses the trigger at the start position or at a greater value.
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
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](./setmodeslopefeedback%28startposition,endposition,startstrength,endstrength%29.md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/positionalresistivestrengths)*