# discretePositionCount

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

The number of discrete control positions that the DualSense adaptive triggers support.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
class var discretePositionCount: Int { get }
```

```c
GCDualSenseAdaptiveTriggerDiscretePositionCount
```

## Discussion

You can configure each of these positions separately in multiposition feedback and vibration modes.

## See Also

### Related Documentation
- [func setModeFeedback(resistiveStrengths: GCDualSenseAdaptiveTrigger.PositionalResistiveStrengths)](./setmodefeedback%28resistivestrengths%29.md)
  Sets the mode to provide feedback with the specified strengths for each possible trigger position.
- [func setModeVibration(amplitudes: GCDualSenseAdaptiveTrigger.PositionalAmplitudes, frequency: Float)](./setmodevibration%28amplitudes,frequency%29.md)
  Sets the mode to vibrate with the specified amplitudes for each possible trigger position.
### Getting the arm position
- [var armPosition: Float](./armposition.md)
  The position of the trigger’s arm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/discretepositioncount)*