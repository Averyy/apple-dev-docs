# setCalibrationMode(calibrationMode:level:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setCalibrationMode:(PHASECalibrationMode) calibrationMode level:(double) level;
```

## Parameters

- `calibrationMode`: A given strategy for sound pressure level. For a consistent user experience across platforms and output devices, choose [`PHASECalibrationMode.absoluteSpl`](../phasecalibrationmode/absolutespl.md) or [`PHASECalibrationMode.relativeSpl`](../phasecalibrationmode/relativespl.md).
- `level`: The loudness. The calibration mode determines this value’s unit and range.

## See Also

### Calibrating Loudness
- [var calibrationMode: PHASECalibrationMode](./calibrationmode.md)
  A sound pressure level strategy for loudness correction.
- [var level: Double](./level.md)
  The node’s loudness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:))*