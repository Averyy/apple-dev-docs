# PKStrokePointReference

**Framework**: PencilKit  
**Kind**: class

A class that represents the properties of a specific point along a stroke’s path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKStrokePointReference
```

## Topics

### Creating a stroke point object
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat)](pkstrokepointreference/init(location:timeoffset:size:opacity:force:azimuth:altitude:).md)
  Creates a new point with the provided properties.
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat)](pkstrokepointreference/init(location:timeoffset:size:opacity:force:azimuth:altitude:secondaryscale:).md)
### Getting the point’s location
- [var location: CGPoint](pkstrokepointreference/location.md)
  The location of this point.
- [var timeOffset: TimeInterval](pkstrokepointreference/timeoffset.md)
  The time offset since the start of the stroke path in seconds.
### Getting the point’s touch data
- [var altitude: CGFloat](pkstrokepointreference/altitude.md)
  The altitude of this point in radians.
- [var azimuth: CGFloat](pkstrokepointreference/azimuth.md)
  The azimuth of this point in radians.
- [var force: CGFloat](pkstrokepointreference/force.md)
  The amount of force applied by the touch.
### Getting the point’s drawing data
- [var size: CGSize](pkstrokepointreference/size.md)
  The size of the point.
- [var opacity: CGFloat](pkstrokepointreference/opacity.md)
  Opacity of the point.
- [var secondaryScale: CGFloat](pkstrokepointreference/secondaryscale.md)
### Initializers
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat, threshold: CGFloat)](pkstrokepointreference/init(location:timeoffset:size:opacity:force:azimuth:altitude:secondaryscale:threshold:).md)
  Create a new point with the provided properties.
### Instance Properties
- [var threshold: CGFloat](pkstrokepointreference/threshold.md)
  The threshold for clipping the stroke rendering.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepointreference)*