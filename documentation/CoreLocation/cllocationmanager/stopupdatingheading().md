# stopUpdatingHeading()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Stops the generation of heading updates.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func stopUpdatingHeading()
```

```objc
- (void) stopUpdatingHeading;
```

## Discussion

Call this method whenever your code no longer needs to receive heading-related events. Disabling event delivery gives the receiver the option of disabling the appropriate hardware (and thereby saving power) when no clients need location data. You can always restart the generation of heading updates by calling the [`startUpdatingHeading()`](./startupdatingheading%28%29.md) method again.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the heading service
- [func startUpdatingHeading()](./startupdatingheading%28%29.md)
  Starts the generation of updates that report the user’s current heading.
- [func dismissHeadingCalibrationDisplay()](./dismissheadingcalibrationdisplay%28%29.md)
  Dismisses the heading calibration view from the screen immediately.
- [var headingFilter: CLLocationDegrees](./headingfilter.md)
  The minimum angular change in degrees required to generate new heading events.
- [let kCLHeadingFilterNone: CLLocationDegrees](../kclheadingfilternone.md)
  A constant indicating that all header values should be reported.
- [typealias CLLocationDegrees](../cllocationdegrees.md)
  A latitude or longitude value specified in degrees.
- [var headingBody: (any CLBodyIdentifiable)?](./headingbody.md)
  A physical body or view that defines the reference orientation for heading calculations.
- [var headingOrientation: CLDeviceOrientation](./headingorientation.md)
  The device orientation to use when computing heading values.
- [enum CLDeviceOrientation](../cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopupdatingheading())*