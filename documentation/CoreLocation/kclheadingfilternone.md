# kCLHeadingFilterNone

**Framework**: Core Location  
**Kind**: var

A constant indicating that all header values should be reported.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCLHeadingFilterNone: CLLocationDegrees
```

#### Discussion

Use this constant to indicate that any change to the heading, regardless of how small, should be reported.

## See Also

- [func startUpdatingHeading()](cllocationmanager/startupdatingheading.md)
  Starts the generation of updates that report the user’s current heading.
- [func stopUpdatingHeading()](cllocationmanager/stopupdatingheading.md)
  Stops the generation of heading updates.
- [func dismissHeadingCalibrationDisplay()](cllocationmanager/dismissheadingcalibrationdisplay.md)
  Dismisses the heading calibration view from the screen immediately.
- [var headingFilter: CLLocationDegrees](cllocationmanager/headingfilter.md)
  The minimum angular change in degrees required to generate new heading events.
- [var headingOrientation: CLDeviceOrientation](cllocationmanager/headingorientation.md)
  The device orientation to use when computing heading values.
- [enum CLDeviceOrientation](cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kclheadingfilternone)*