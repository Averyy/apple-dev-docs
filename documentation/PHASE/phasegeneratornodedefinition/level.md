# level

**Framework**: PHASE  
**Kind**: property

The node’s loudness.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var level: Double { get }
```

#### Discussion

The default value is `1`. To set a value, call [`setCalibrationMode(calibrationMode:level:)`](phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:).md).

## See Also

- [func setCalibrationMode(calibrationMode: PHASECalibrationMode, level: Double)](phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:).md)
  Selects a loudness correction strategy and reference level.
- [var calibrationMode: PHASECalibrationMode](phasegeneratornodedefinition/calibrationmode.md)
  A sound pressure level strategy for loudness correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/level)*