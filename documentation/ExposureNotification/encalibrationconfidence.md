# ENCalibrationConfidence

**Framework**: Exposure Notification  
**Kind**: enum  
**Role**: Enumeration

The transmitting device’s calibration confidence.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
enum ENCalibrationConfidence
```

```c
enum ENCalibrationConfidence : uint8_t;
```

## Overview

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## Topics

### Enumeration Cases
- [ENCalibrationConfidence.high](./encalibrationconfidence/high.md)
  The highest confidence in the calibration data.
- [ENCalibrationConfidence.medium](./encalibrationconfidence/medium.md)
  The medium confidence in the calibration data.
- [ENCalibrationConfidence.low](./encalibrationconfidence/low.md)
  The average confidence in the calibration data.
- [ENCalibrationConfidence.lowest](./encalibrationconfidence/lowest.md)
  No confidence in the calibration data.
### Initializers
- [init?(rawValue: UInt8)](./encalibrationconfidence/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [Attenuation](./attenuation.md)
  The minimum and maximum signal attenuations.
- [Risk Level](./risk-level.md)
  The minimum and maximum risk levels.
- [Risk Level Value](./risk-level-value.md)
  The minimum and maximum risk level values.
- [Risk Score](./risk-score.md)
  The minimum and maximum risk score.
- [Risk Weight](./risk-weight.md)
  The minimum, default, and maximum risk weights.
- [struct ENActivityFlags](./enactivityflags.md)
  Activities that occur while the app isn’t running.
- [enum ENDiagnosisReportType](./endiagnosisreporttype.md)
  The type of a report that describes the origin of a diagnosis.
- [enum ENInfectiousness](./eninfectiousness.md)
  The degree to which a person’s symptoms may indicate transmission risk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/encalibrationconfidence)*