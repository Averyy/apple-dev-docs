# attenuationDurations

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

An array of durations at specific radio signal attenuations.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var attenuationDurations: [NSNumber] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSNumber *> * attenuationDurations;
```

## Discussion

An array that contains the duration, in seconds, at certain attenuations, using an aggregated maximum exposures of 30 minutes.

`array[0]` =  Sum of durations for all exposures when the attenuation value was `Attenuation <= X`.

`array[1]` =  Sum of durations for all exposures when attenuation value was `X < Attenuation <= Y`.

`array[2]` =  Sum of durations for all exposures when attenuation value was `Y < Attenuation`.

Use the [`attenuationDurationThresholds`](../enexposureconfiguration/attenuationdurationthresholds.md) to configure the `X` and `Y` values.

## See Also

### Exposure Criteria
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
- [var daysSinceOnsetOfSymptoms: Int](./dayssinceonsetofsymptoms.md)
  The number of days since the onset of symptoms.
- [var diagnosisReportType: ENDiagnosisReportType](./diagnosisreporttype.md)
  The method used to report the positive diagnosis.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](../endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo/attenuationdurations)*