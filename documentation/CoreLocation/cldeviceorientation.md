# CLDeviceOrientation

**Framework**: Core Location  
**Kind**: enum

Constants indicating the physical orientation of the device.

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
enum CLDeviceOrientation
```

## Topics

### Device Orientations
- [CLDeviceOrientation.unknown](cldeviceorientation/unknown.md)
  The orientation is currently not known.
- [CLDeviceOrientation.portrait](cldeviceorientation/portrait.md)
  The device is in portrait mode, with the device held upright and the home button at the bottom.
- [CLDeviceOrientation.portraitUpsideDown](cldeviceorientation/portraitupsidedown.md)
  The device is in portrait mode but upside down, with the device held upright and the home button at the top.
- [CLDeviceOrientation.landscapeLeft](cldeviceorientation/landscapeleft.md)
  The device is in landscape mode, with the device held upright and the home button on the right side.
- [CLDeviceOrientation.landscapeRight](cldeviceorientation/landscaperight.md)
  The device is in landscape mode, with the device held upright and the home button on the left side.
- [CLDeviceOrientation.faceUp](cldeviceorientation/faceup.md)
  The device is held parallel to the ground with the screen facing upwards.
- [CLDeviceOrientation.faceDown](cldeviceorientation/facedown.md)
  The device is held parallel to the ground with the screen facing downwards.
### Initializers
- [init?(rawValue: Int32)](cldeviceorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var headingOrientation: CLDeviceOrientation](cllocationmanager/headingorientation.md)
  The device orientation to use when computing heading values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cldeviceorientation)*