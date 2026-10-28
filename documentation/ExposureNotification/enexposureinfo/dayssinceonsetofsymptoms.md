# daysSinceOnsetOfSymptoms

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The number of days since the onset of symptoms.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var daysSinceOnsetOfSymptoms: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger daysSinceOnsetOfSymptoms;
```

## Discussion

The default value is `ENDaysSinceOnsetOfSymptomsUnknown`.

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
- [var totalRiskScoreFullRange: Double](./totalriskscorefullrange.md)
  The value that represents the full-range total risk score the framework calculates for this exposure incident.
- [var transmissionRiskLevel: ENRiskLevel](./transmissionrisklevel.md)
  The transmission risk associated with a diagnosis key.
- [typealias ENAttenuation](../enattenuation.md)
  The signal strength value.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The metadata associated with the exposure information.
- [var diagnosisReportType: ENDiagnosisReportType](./diagnosisreporttype.md)
  The method used to report the positive diagnosis.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](../endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo/dayssinceonsetofsymptoms)*