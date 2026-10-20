# totalRiskScoreFullRange

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The value that represents the full-range total risk score the framework calculates for this exposure incident.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var totalRiskScoreFullRange: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double totalRiskScoreFullRange;
```

#### Discussion

This value is not limited by [`ENRiskScoreMax`](../enriskscoremax.md).

## See Also

### Exposure Criteria
- [var attenuationDurations: [NSNumber]](./attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var attenuationValue: ENAttenuation](./attenuationvalue.md)
  The attenutation risk level value for the exposure.
- [var date: Date](./date.md)
  The date the exposure occurred.
- [var duration: TimeInterval](./duration.md)
  The length of time that the contact was in proximity to the user.
- [var totalRiskScore: ENRiskScore](./totalriskscore.md)
  The value that represents the total risk score the framework calculates for this exposure incident.
- [var transmissionRiskLevel: ENRiskLevel](./transmissionrisklevel.md)
  The transmission risk associated with a diagnosis key.
- [typealias ENAttenuation](../enattenuation.md)
  The signal strength value.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The metadata associated with the exposure information.
- [var daysSinceOnsetOfSymptoms: Int](./dayssinceonsetofsymptoms.md)
  The number of days since the onset of symptoms.
- [var diagnosisReportType: ENDiagnosisReportType](./diagnosisreporttype.md)
  The method used to report the positive diagnosis.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](../endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo/totalriskscorefullrange)*