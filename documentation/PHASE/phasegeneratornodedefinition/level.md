# level

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) double level;
```

## Discussion

The default value is `1`. To set a value, call [`setCalibrationMode(calibrationMode:level:)`](./setcalibrationmode%28calibrationmode,level%29.md).

## See Also

### Calibrating Loudness
- [func setCalibrationMode(calibrationMode: PHASECalibrationMode, level: Double)](./setcalibrationmode%28calibrationmode,level%29.md)
  Selects a loudness correction strategy and reference level.
- [var calibrationMode: PHASECalibrationMode](./calibrationmode.md)
  A sound pressure level strategy for loudness correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/level)*