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

When computing heading values, the location manager assumes that the top of the device in portrait mode represents due north (0 degrees) by default. For apps that run in other orientations, this property allows you to specify which device orientation you want the location manager to use as the reference point for due north.

Setting the value of this property to [`CLDeviceOrientation.unknown`](cldeviceorientation/unknown.md), [`CLDeviceOrientation.faceUp`](cldeviceorientation/faceup.md), or [`CLDeviceOrientation.faceDown`](cldeviceorientation/facedown.md) has no effect on the orientation reference point, and the system retains the original reference point instead.

Changing the value in this property affects only heading values reported after the change.

## Topics

### Heading configuration
- [var headingBody: (any CLBodyIdentifiable)?](cllocationmanager/headingbody.md)
  A physical body or view that defines the reference orientation for heading calculations.
- [enum CLDeviceOrientation](cldeviceorientation.md)
  Constants indicating the physical orientation of the device.

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
- [typealias CLLocationDegrees](cllocationdegrees.md)
  A latitude or longitude value specified in degrees.
- [var headingBody: (any CLBodyIdentifiable)?](cllocationmanager/headingbody.md)
  A physical body or view that defines the reference orientation for heading calculations.
- [enum CLDeviceOrientation](cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingorientation)*