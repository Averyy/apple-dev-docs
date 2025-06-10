# headingOrientation

**Framework**: Core Location  
**Kind**: property

The device orientation to use when computing heading values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var headingOrientation: CLDeviceOrientation { get set }
```

## Mentions

- [Getting heading and course information](getting-heading-and-course-information.md)

#### Discussion

When computing heading values, the location manager assumes that the top of the device in portrait mode represents due north (0 degrees) by default. For apps that run in other orientations, this may not always be the most convenient orientation. This property allows you to specify which device orientation you want the location manager to use as the reference point for due north.

Although you can set the value of this property to [`CLDeviceOrientation.unknown`](cldeviceorientation/unknown.md), [`CLDeviceOrientation.faceUp`](cldeviceorientation/faceup.md), or [`CLDeviceOrientation.faceDown`](cldeviceorientation/facedown.md), doing so has no effect on the orientation reference point. The original reference point is retained instead.

Changing the value in this property affects only those heading values reported after the change is made.

## See Also

- [func startUpdatingHeading()](cllocationmanager/startupdatingheading.md)
  Starts the generation of updates that report the user’s current heading.
- [func stopUpdatingHeading()](cllocationmanager/stopupdatingheading.md)
  Stops the generation of heading updates.
- [func dismissHeadingCalibrationDisplay()](cllocationmanager/dismissheadingcalibrationdisplay.md)
  Dismisses the heading calibration view from the screen immediately.
- [var headingFilter: CLLocationDegrees](cllocationmanager/headingfilter.md)
  The minimum angular change in degrees required to generate new heading events.
- [let kCLHeadingFilterNone: CLLocationDegrees](kclheadingfilternone.md)
  A constant indicating that all header values should be reported.
- [enum CLDeviceOrientation](cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingorientation)*