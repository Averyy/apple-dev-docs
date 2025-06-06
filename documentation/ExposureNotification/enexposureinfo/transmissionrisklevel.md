# transmissionRiskLevel

**Framework**: Exposure Notification  
**Kind**: property

The transmission risk associated with a diagnosis key.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var transmissionRiskLevel: ENRiskLevel { get }
```

#### Discussion

Each app defines its own meaning for each of the risk levels (0-7).

Consistent Transmission Risk Levels across regions facilitate roaming, therefore it’s recommended that the Transmission Risk Levels describe the type of report. The supported report types are determined by the public health authority for each region. Your app must verify the report type with a public health authority before submitting it.

Recommended report types for the different risk levels are:

- `0` = Unused/Custom
- `1` = Confirmed test: Low transmission risk level
- `2` = Confirmed test: Standard transmission risk level
- `3` = Confirmed test: High transmission risk level
- `4` = Confirmed clinical diagnosis
- `5` = Self report
- `6` = Negative case
- `7` = Recursive case

## See Also

- [var attenuationDurations: [NSNumber]](enexposureinfo/attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var attenuationValue: ENAttenuation](enexposureinfo/attenuationvalue.md)
  The attenutation risk level value for the exposure.
- [var date: Date](enexposureinfo/date.md)
  The date the exposure occurred.
- [var duration: TimeInterval](enexposureinfo/duration.md)
  The length of time that the contact was in proximity to the user.
- [var totalRiskScore: ENRiskScore](enexposureinfo/totalriskscore.md)
  The value that represents the total risk score the framework calculates for this exposure incident.
- [var totalRiskScoreFullRange: Double](enexposureinfo/totalriskscorefullrange.md)
  The value that represents the full-range total risk score the framework calculates for this exposure incident.
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

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo/transmissionrisklevel)*