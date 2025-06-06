# setCalibrationMode(calibrationMode:level:)

**Framework**: PHASE  
**Kind**: method

Selects a loudness correction strategy and reference level.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setCalibrationMode(calibrationMode: PHASECalibrationMode, level: Double)
```

## Parameters

- `calibrationMode`: A given strategy for sound pressure level. For a consistent user experience across platforms and output devices, choose   or  .
- `level`: The loudness. The calibration mode determines this value’s unit and range.

## See Also

- [var calibrationMode: PHASECalibrationMode](phasegeneratornodedefinition/calibrationmode.md)
  A sound pressure level strategy for loudness correction.
- [var level: Double](phasegeneratornodedefinition/level.md)
  The node’s loudness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:))*