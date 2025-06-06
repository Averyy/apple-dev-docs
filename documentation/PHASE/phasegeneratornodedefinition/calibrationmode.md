# calibrationMode

**Framework**: PHASE  
**Kind**: property

A sound pressure level strategy for loudness correction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var calibrationMode: PHASECalibrationMode { get }
```

#### Discussion

The default value is [`PHASECalibrationMode.none`](phasecalibrationmode/none.md). To set a value, call [`setCalibrationMode(calibrationMode:level:)`](phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:).md).

## See Also

- [func setCalibrationMode(calibrationMode: PHASECalibrationMode, level: Double)](phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:).md)
  Selects a loudness correction strategy and reference level.
- [var level: Double](phasegeneratornodedefinition/level.md)
  The node’s loudness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/calibrationmode)*