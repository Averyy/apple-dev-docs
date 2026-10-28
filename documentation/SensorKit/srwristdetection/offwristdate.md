# offWristDate

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The date and time that the user takes their Apple Watch off their wrist.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var offWristDate: Date? { get }
```

```objc
@property (strong, readonly, nullable) NSDate * offWristDate;
```

## Discussion

Use this property to compute the duration that the user wears their Apple Watch.

The initial value of the [`offWristDate`](./offwristdate.md) property is the current date and the [`onWristDate`](./onwristdate.md) property is [`nil`](../../ObjectiveC/nil-227m0.md). The system changes the value of these properties as follows:

- When the user puts on their Apple Watch, the [`onWristDate`](./onwristdate.md) property becomes the current date and the [`offWristDate`](./offwristdate.md) property remains the same.
- When the user takes off their Apple Watch, the [`offWristDate`](./offwristdate.md) property becomes the current date, and the [`onWristDate`](./onwristdate.md) property remains the same.

## See Also

### Inspecting Watch Configuration
- [var crownOrientation: SRWristDetection.CrownOrientation](./crownorientation-swift.property.md)
  A value that indicates the direction the Digital Crown faces with respect to the user.
- [SRWristDetection.CrownOrientation](./crownorientation-swift.enum.md)
  Directions the Digital Crown can face with respect to the wearer.
- [var onWrist: Bool](./onwrist.md)
  A value that indicates whether the watch is on the user’s wrist.
- [var onWristDate: Date?](./onwristdate.md)
  The date and time that the user puts their Apple Watch on their wrist.
- [var wristLocation: SRWristDetection.WristLocation](./wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.
- [SRWristDetection.WristLocation](./wristlocation-swift.enum.md)
  Preferences for where a user wears a watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)*