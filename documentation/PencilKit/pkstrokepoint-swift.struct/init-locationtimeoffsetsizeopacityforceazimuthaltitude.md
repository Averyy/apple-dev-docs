# init(location:timeOffset:size:opacity:force:azimuth:altitude:)

**Framework**: PencilKit  
**Kind**: init

Creates a new point with the provided properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat)
```

## Parameters

- `location`: The location of this point.
- `timeOffset`: The time offset since the start of this stoke path in seconds.
- `size`: The size of this point.
- `opacity`: The opacity of this point, ranging from   to  .
- `force`: The amount of force used to create this point.
- `azimuth`: The azimuth of this point in radians.
- `altitude`: The altitude of this point in radians.

## See Also

- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat)](pkstrokepoint-swift.struct/init(location:timeoffset:size:opacity:force:azimuth:altitude:secondaryscale:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/init(location:timeoffset:size:opacity:force:azimuth:altitude:))*