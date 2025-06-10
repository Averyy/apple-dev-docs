# duration

**Framework**: Exposure Notification  
**Kind**: property

The length of time that the contact was in proximity to the user.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

When reporting the duration of an exposure, the values are stored as seconds rounded up to the next minute. A duration value caps at 30 minutes (1800 seconds).

> **Note**:  In iOS 13.5, duration values are rounded up to the next 5-minute interval.

## See Also

- [var attenuationDurations: [NSNumber]](enexposureinfo/attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var attenuationValue: ENAttenuation](enexposureinfo/attenuationvalue.md)
  The attenutation risk level value for the exposure.
- [var date: Date](enexposureinfo/date.md)
  The date the exposure occurred.
- [var totalRiskScore: ENRiskScore](enexposureinfo/totalriskscore.md)
  The value that represents the total risk score the framework calculates for this exposure incident.
- [var totalRiskScoreFullRange: Double](enexposureinfo/totalriskscorefullrange.md)
  The value that represents the full-range total risk score the framework calculates for this exposure incident.
- [var transmissionRiskLevel: ENRiskLevel](enexposureinfo/transmissionrisklevel.md)
  The transmission risk associated with a diagnosis key.
- [typealias ENAttenuation](enattenuation.md)
  The signal strength value.
- [var metadata: [AnyHashable : Any]?](enexposureinfo/metadata.md)
  The metadata associated with the exposure information.
- [var daysSinceOnsetOfSymptoms: Int](enexposureinfo/dayssinceonsetofsymptoms.md)
  The number of days since the onset of symptoms.
- [var diagnosisReportType: ENDiagnosisReportType](enexposureinfo/diagnosisreporttype.md)
  The method used to report the positive diagnosis.
- [let ENDaysSinceOnsetOfSymptomsUnknown: Int](endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo/duration)*