# ENInfectiousness

**Framework**: Exposure Notification  
**Kind**: enum

The degree to which a person’s symptoms may indicate transmission risk.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
enum ENInfectiousness
```

#### Overview

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## Topics

### Enumeration Cases
- [ENInfectiousness.high](eninfectiousness/high.md)
  The user is highly infectious.
- [ENInfectiousness.none](eninfectiousness/none.md)
  The user is not infectious.
- [ENInfectiousness.standard](eninfectiousness/standard.md)
  The user is mildly infectious.
### Initializers
- [init?(rawValue: UInt32)](eninfectiousness/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Attenuation](attenuation.md)
  The minimum and maximum signal attenuations.
- [Risk Level](risk-level.md)
  The minimum and maximum risk levels.
- [Risk Level Value](risk-level-value.md)
  The minimum and maximum risk level values.
- [Risk Score](risk-score.md)
  The minimum and maximum risk score.
- [Risk Weight](risk-weight.md)
  The minimum, default, and maximum risk weights.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.
- [enum ENCalibrationConfidence](encalibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [enum ENDiagnosisReportType](endiagnosisreporttype.md)
  The type of a report that describes the origin of a diagnosis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/eninfectiousness)*