# ENExposureInfo

**Framework**: Exposure Notification  
**Kind**: class

The incident information related to a potential exposure.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureInfo
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.5 and later. It isn’t supported for apps with [`ENAPIVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion) set to `2` in the `Info.plist` file. Instead, [`getExposureWindows(summary:completionHandler:)`](enmanager/getexposurewindows(summary:completionhandler:).md) provides an array of [`ENExposureWindow`](enexposurewindow.md) objects.

This class carries information about an exposure incident.

## Topics

### Exposure Criteria
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [typealias ENRiskScore](enriskscore.md)
  A value signifying the risk of an exposure event.
- [typealias ENRiskLevel](enrisklevel.md)
  The user’s estimated risk of exposure.
- [typealias ENRiskLevelValue](enrisklevelvalue.md)
  The value associated with a particular risk level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureinfo)*