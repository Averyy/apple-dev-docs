# FoveatedStreamingProvider.FocusRegion

**Framework**: Foveated Streaming  
**Kind**: struct

Eye input data that describes the approximate region that the end user is looking, relative to the device pose.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FocusRegion
```

## Topics

### Instance Properties
- [let direction: simd_float3](foveatedstreamingprovider/focusregion/direction.md)
  The direction of the user’s gaze in device-relative coordinates.
- [let distance: Float](foveatedstreamingprovider/focusregion/distance.md)
  The estimated distance to the user’s focal point, in meters.
- [let timestamp: TimeInterval](foveatedstreamingprovider/focusregion/timestamp.md)
  The timestamp at which this focus region sample was captured, in the format returned by `CACurrentMediaTime()`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/focusregion)*