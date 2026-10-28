# scanInstances

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

An array of scans corresponding to a beacon associated with an exposure.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var scanInstances: [ENScanInstance] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<ENScanInstance *> * scanInstances;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

### Getting Window Properties
- [var calibrationConfidence: ENCalibrationConfidence](./calibrationconfidence.md)
  The transmitting device’s calibration confidence.
- [var date: Date](./date.md)
  The date that the exposure occurred.
- [var diagnosisReportType: ENDiagnosisReportType](./diagnosisreporttype.md)
  The report type of the observed diagnosis.
- [var infectiousness: ENInfectiousness](./infectiousness.md)
  How infectious the user is, based on the number of days since the onset of symptoms.
- [var variantOfConcernType: ENVariantOfConcernType](./variantofconcerntype.md)
  The variant of concern associated with this user.
- [enum ENVariantOfConcernType](../envariantofconcerntype.md)
  A set of user-definable types that indicate variants of concern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposurewindow/scaninstances)*