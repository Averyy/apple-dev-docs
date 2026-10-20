# SRWristDetection.WristLocation

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Preferences for where a user wears a watch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum WristLocation
```

```c
enum SRWristLocation : NSInteger;
```

## Topics

### Wrist Preferences
- [SRWristDetection.WristLocation.left](./wristlocation-swift.enum/left.md)
  Indicates that the user wears a watch on the left wrist.
- [SRWristDetection.WristLocation.right](./wristlocation-swift.enum/right.md)
  Indicates that the user wears a watch on the right wrist.
### Initializers
- [init?(rawValue: Int)](./wristlocation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var offWristDate: Date?](./offwristdate.md)
  The date and time that the user takes their Apple Watch off their wrist.
- [var wristLocation: SRWristDetection.WristLocation](./wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)*