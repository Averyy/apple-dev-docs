# ENDiagnosisReportType

**Framework**: Exposure Notification  
**Kind**: enum  
**Role**: Enumeration

The type of a report that describes the origin of a diagnosis.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
enum ENDiagnosisReportType
```

```c
enum ENDiagnosisReportType : uint32_t;
```

## Overview

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## Topics

### Enumeration Cases
- [ENDiagnosisReportType.confirmedClinicalDiagnosis](./endiagnosisreporttype/confirmedclinicaldiagnosis.md)
  The report comes from a confirmed clinical diagnosis.
- [ENDiagnosisReportType.confirmedTest](./endiagnosisreporttype/confirmedtest.md)
  The report comes from a confirmed test.
- [ENDiagnosisReportType.recursive](./endiagnosisreporttype/recursive.md)
  The report comes from a person determined positive based on exposure to another person confirmed positive.
- [ENDiagnosisReportType.revoked](./endiagnosisreporttype/revoked.md)
  The report is a negative test.
- [ENDiagnosisReportType.selfReported](./endiagnosisreporttype/selfreported.md)
  The report comes from the user, without health authority involvement.
- [ENDiagnosisReportType.unknown](./endiagnosisreporttype/unknown.md)
  The report is an unknown type or is not available.
### Initializers
- [init?(rawValue: UInt32)](./endiagnosisreporttype/init%28rawvalue%29.md)

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
- [enum ENCalibrationConfidence](./encalibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [enum ENInfectiousness](./eninfectiousness.md)
  The degree to which a person’s symptoms may indicate transmission risk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endiagnosisreporttype)*