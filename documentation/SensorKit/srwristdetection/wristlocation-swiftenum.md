# SRWristDetection.WristLocation

**Framework**: SensorKit  
**Kind**: enum

Preferences for where a user wears a watch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum WristLocation
```

## Topics

### Wrist Preferences
- [SRWristDetection.WristLocation.left](srwristdetection/wristlocation-swift.enum/left.md)
  Indicates that the user wears a watch on the left wrist.
- [SRWristDetection.WristLocation.right](srwristdetection/wristlocation-swift.enum/right.md)
  Indicates that the user wears a watch on the right wrist.
### Initializers
- [init?(rawValue: Int)](srwristdetection/wristlocation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var crownOrientation: SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.property.md)
  A value that indicates the direction the Digital Crown faces with respect to the user.
- [SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.enum.md)
  Directions the Digital Crown can face with respect to the wearer.
- [var onWrist: Bool](srwristdetection/onwrist.md)
  A value that indicates whether the watch is on the user’s wrist.
- [var onWristDate: Date?](srwristdetection/onwristdate.md)
  The date and time that the user puts their Apple Watch on their wrist.
- [var offWristDate: Date?](srwristdetection/offwristdate.md)
  The date and time that the user takes their Apple Watch off their wrist.
- [var wristLocation: SRWristDetection.WristLocation](srwristdetection/wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)*