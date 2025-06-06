# onWristDate

**Framework**: SensorKit  
**Kind**: property

The date and time that the user puts their Apple Watch on their wrist.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var onWristDate: Date? { get }
```

#### Discussion

Use this property to compute the duration that the user wears their Apple Watch.

The initial value of the [`onWristDate`](srwristdetection/onwristdate.md) property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) and the [`offWristDate`](srwristdetection/offwristdate.md) property is the current date. The system changes the value of these properties as follows:

- When the user puts on their Apple Watch, the [`onWristDate`](srwristdetection/onwristdate.md) property becomes the current date and the [`offWristDate`](srwristdetection/offwristdate.md) property remains the same.
- When the user takes off their Apple Watch, the [`offWristDate`](srwristdetection/offwristdate.md) property becomes the current date, and the [`onWristDate`](srwristdetection/onwristdate.md) property remains the same.

## See Also

- [var crownOrientation: SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.property.md)
  A value that indicates the direction the Digital Crown faces with respect to the user.
- [SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.enum.md)
  Directions the Digital Crown can face with respect to the wearer.
- [var onWrist: Bool](srwristdetection/onwrist.md)
  A value that indicates whether the watch is on the user’s wrist.
- [var offWristDate: Date?](srwristdetection/offwristdate.md)
  The date and time that the user takes their Apple Watch off their wrist.
- [var wristLocation: SRWristDetection.WristLocation](srwristdetection/wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.
- [SRWristDetection.WristLocation](srwristdetection/wristlocation-swift.enum.md)
  Preferences for where a user wears a watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)*