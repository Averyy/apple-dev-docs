# date

**Framework**: Exposure Notification  
**Kind**: property

The date that the exposure occurred.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var date: Date { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

 This property is available in iOS 12.5, and in iOS 13.7 and later.

The framework stores the date in Universal Coordinated Time (UTC) and rounds the value to the beginning of the exposure day. For example, a date and time of February 1, 2021 at 10:14 UTC rounds to February 1, 2021 at 00:00 UTC.

## See Also

- [var calibrationConfidence: ENCalibrationConfidence](enexposurewindow/calibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [var diagnosisReportType: ENDiagnosisReportType](enexposurewindow/diagnosisreporttype.md)
  The report type of the observed diagnosis.
- [var infectiousness: ENInfectiousness](enexposurewindow/infectiousness.md)
  How infectious the user is, based on the number of days since the onset of symptoms.
- [var scanInstances: [ENScanInstance]](enexposurewindow/scaninstances.md)
  An array of scans corresponding to a beacon associated with an exposure.
- [var variantOfConcernType: ENVariantOfConcernType](enexposurewindow/variantofconcerntype.md)
  The variant of concern associated with this user.
- [enum ENVariantOfConcernType](envariantofconcerntype.md)
  A set of user-definable types that indicate variants of concern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposurewindow/date)*