# crownOrientation

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates the direction the Digital Crown faces with respect to the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var crownOrientation: SRWristDetection.CrownOrientation { get }
```

```objc
@property (readonly) SRCrownOrientation crownOrientation;
```

## See Also

### Inspecting Watch Configuration
- [SRWristDetection.CrownOrientation](./crownorientation-swift.enum.md)
  Directions the Digital Crown can face with respect to the wearer.
- [var onWrist: Bool](./onwrist.md)
  A value that indicates whether the watch is on the user’s wrist.
- [var onWristDate: Date?](./onwristdate.md)
  The date and time that the user puts their Apple Watch on their wrist.
- [var offWristDate: Date?](./offwristdate.md)
  The date and time that the user takes their Apple Watch off their wrist.
- [var wristLocation: SRWristDetection.WristLocation](./wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.
- [SRWristDetection.WristLocation](./wristlocation-swift.enum.md)
  Preferences for where a user wears a watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)*