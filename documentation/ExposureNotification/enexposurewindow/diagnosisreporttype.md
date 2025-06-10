# diagnosisReportType

**Framework**: Exposure Notification  
**Kind**: property

The report type of the observed diagnosis.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var diagnosisReportType: ENDiagnosisReportType { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

- [var calibrationConfidence: ENCalibrationConfidence](enexposurewindow/calibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [var date: Date](enexposurewindow/date.md)
  The date that the exposure occurred.
- [var infectiousness: ENInfectiousness](enexposurewindow/infectiousness.md)
  How infectious the user is, based on the number of days since the onset of symptoms.
- [var scanInstances: [ENScanInstance]](enexposurewindow/scaninstances.md)
  An array of scans corresponding to a beacon associated with an exposure.
- [var variantOfConcernType: ENVariantOfConcernType](enexposurewindow/variantofconcerntype.md)
  The variant of concern associated with this user.
- [enum ENVariantOfConcernType](envariantofconcerntype.md)
  A set of user-definable types that indicate variants of concern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposurewindow/diagnosisreporttype)*