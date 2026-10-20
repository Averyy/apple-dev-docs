# SRWristDetection.CrownOrientation

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Directions the Digital Crown can face with respect to the wearer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CrownOrientation
```

```c
enum SRCrownOrientation : NSInteger;
```

## Topics

### Orientations
- [SRWristDetection.CrownOrientation.left](./crownorientation-swift.enum/left.md)
  Indicates that the Digital Crown faces to the left with respect to the wearer.
- [SRWristDetection.CrownOrientation.right](./crownorientation-swift.enum/right.md)
  Indicates that the Digital Crown faces to the right with respect to the wearer.
### Initializers
- [init?(rawValue: Int)](./crownorientation-swift.enum/init%28rawvalue%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)*