# variantOfConcernType

**Framework**: Exposure Notification  
**Kind**: property

The variant of concern associated with this user.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+

## Declaration

```swift
var variantOfConcernType: ENVariantOfConcernType { get }
```

#### Discussion

The Public Health Authority (PHA) has control over defining the meaning of the types that indicate variants of concern.

## See Also

- [var calibrationConfidence: ENCalibrationConfidence](enexposurewindow/calibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [var date: Date](enexposurewindow/date.md)
  The date that the exposure occurred.
- [var diagnosisReportType: ENDiagnosisReportType](enexposurewindow/diagnosisreporttype.md)
  The report type of the observed diagnosis.
- [var infectiousness: ENInfectiousness](enexposurewindow/infectiousness.md)
  How infectious the user is, based on the number of days since the onset of symptoms.
- [var scanInstances: [ENScanInstance]](enexposurewindow/scaninstances.md)
  An array of scans corresponding to a beacon associated with an exposure.
- [enum ENVariantOfConcernType](envariantofconcerntype.md)
  A set of user-definable types that indicate variants of concern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposurewindow/variantofconcerntype)*