# CLLocationDirection

**Framework**: Core Location  
**Kind**: typealias

An azimuth that is measured in degrees relative to true north.

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
typealias CLLocationDirection = Double
```

#### Discussion

Direction values are measured in degrees starting at due north and continue clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is 180 degrees, and so on. A negative value indicates an invalid direction.

## See Also

- [var speed: CLLocationSpeed](cllocation/speed.md)
  The instantaneous speed of the device, measured in meters per second.
- [var speedAccuracy: CLLocationSpeedAccuracy](cllocation/speedaccuracy.md)
  The accuracy of the speed value, measured in meters per second.
- [var course: CLLocationDirection](cllocation/course.md)
  The direction in which the device is traveling, measured in degrees and relative to due north.
- [var courseAccuracy: CLLocationDirectionAccuracy](cllocation/courseaccuracy.md)
  The accuracy of the course value, measured in degrees.
- [typealias CLLocationSpeed](cllocationspeed.md)
  The velocity (measured in meters per second) at which the device is moving.
- [typealias CLLocationSpeedAccuracy](cllocationspeedaccuracy.md)
  The accuracy of a speed.
- [typealias CLLocationDirectionAccuracy](cllocationdirectionaccuracy.md)
  The accuracy of a compass heading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationdirection)*