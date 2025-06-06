# ENExposureWindow

**Framework**: Exposure Notification  
**Kind**: class

A set of scan events from observed beacons within a time span.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureWindow
```

#### Overview

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

 This property is available in iOS 12.5, and in iOS 13.7 and later.

An exposure window contains information about a potential exposure in a 30–minute interval. The system returns an array of exposure windows through the completion handler when the app invokes [`getExposureWindows(summary:completionHandler:)`](enmanager/getexposurewindows(summary:completionhandler:).md). Exposure windows are only available when an app specified an `ENAPIVersion` of `2` in the app’s `Info.plist` file.

## Topics

### Getting Window Properties
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
- [var variantOfConcernType: ENVariantOfConcernType](enexposurewindow/variantofconcerntype.md)
  The variant of concern associated with this user.
- [enum ENVariantOfConcernType](envariantofconcerntype.md)
  A set of user-definable types that indicate variants of concern.

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

- [Configuring Exposure Notifications](configuring-exposure-notifications.md)
  Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- [class ENExposureConfiguration](enexposureconfiguration.md)
  The object that contains parameters for configuring exposure notification risk scoring behavior.
- [class ENScanInstance](enscaninstance.md)
  The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](exposure-parameter-limits.md)
  The limits for the parameters you use in exposure risk calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposurewindow)*