# GCDualSenseAdaptiveTrigger.PositionalAmplitudes

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

The amplitudes for multiple positions on a trigger.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
struct PositionalAmplitudes
```

```c
typedef struct { ... } GCDualSenseAdaptiveTriggerPositionalAmplitudes;
```

## Topics

### Creating multiple amplitudes
- [init(values: (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float))](./positionalamplitudes/init%28values%29.md)
  Creates a positional amplitudes structure with the specified amplitude values.
- [init()](./positionalamplitudes/init%28%29.md)
  Creates an empty positional amplitudes structure.
### Accessing multiple amplitudes
- [var values: (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)](./positionalamplitudes/values.md)
  The amplitude values for possible trigger positions.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Sendable](../../Swift/sendable.md)

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
- [func setModeSlopeFeedback(startPosition: Float, endPosition: Float, startStrength: Float, endStrength: Float)](./setmodeslopefeedback%28startposition,endposition,startstrength,endstrength%29.md)
  Sets the mode to provide feedback when the user tilts the trigger between the start and the end positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/positionalamplitudes)*