# CLLocationDegrees

**Framework**: Core Location  
**Kind**: typealias  
**Role**: Type Alias

A latitude or longitude value specified in degrees.

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
typealias CLLocationDegrees = Double
```

```c
typedef double CLLocationDegrees;
```

## See Also

### Running the heading service
- [func startUpdatingHeading()](./cllocationmanager/startupdatingheading%28%29.md)
  Starts the generation of updates that report the user’s current heading.
- [func stopUpdatingHeading()](./cllocationmanager/stopupdatingheading%28%29.md)
  Stops the generation of heading updates.
- [func dismissHeadingCalibrationDisplay()](./cllocationmanager/dismissheadingcalibrationdisplay%28%29.md)
  Dismisses the heading calibration view from the screen immediately.
- [var headingFilter: CLLocationDegrees](./cllocationmanager/headingfilter.md)
  The minimum angular change in degrees required to generate new heading events.
- [let kCLHeadingFilterNone: CLLocationDegrees](./kclheadingfilternone.md)
  A constant indicating that all header values should be reported.
- [var headingBody: (any CLBodyIdentifiable)?](./cllocationmanager/headingbody.md)
  A physical body or view that defines the reference orientation for heading calculations.
- [var headingOrientation: CLDeviceOrientation](./cllocationmanager/headingorientation.md)
  The device orientation to use when computing heading values.
- [enum CLDeviceOrientation](./cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationdegrees)*