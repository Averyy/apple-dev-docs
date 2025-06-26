# speedAccuracy

**Framework**: Core Location  
**Kind**: property

The accuracy of the speed value, measured in meters per second.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var speedAccuracy: CLLocationSpeedAccuracy { get }
```

#### Discussion

When this property contains `0` or a positive number, the value in the speed property is plus or minus the specified number of meters per second. When this property contains a negative number, the value in the speed property is invalid.

## See Also

- [var speed: CLLocationSpeed](cllocation/speed.md)
  The instantaneous speed of the device, measured in meters per second.
- [var course: CLLocationDirection](cllocation/course.md)
  The direction in which the device is traveling, measured in degrees and relative to due north.
- [var courseAccuracy: CLLocationDirectionAccuracy](cllocation/courseaccuracy.md)
  The accuracy of the course value, measured in degrees.
- [typealias CLLocationSpeed](cllocationspeed.md)
  The velocity (measured in meters per second) at which the device is moving.
- [typealias CLLocationDirection](cllocationdirection.md)
  An azimuth that is measured in degrees relative to true north.
- [typealias CLLocationSpeedAccuracy](cllocationspeedaccuracy.md)
  The accuracy of a speed.
- [typealias CLLocationDirectionAccuracy](cllocationdirectionaccuracy.md)
  The accuracy of a compass heading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/speedaccuracy)*