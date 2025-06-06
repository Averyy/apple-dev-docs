# DeviceAnchor.TrackingState

**Framework**: ARKit  
**Kind**: enum

Values that describe the tracking state of a device anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum TrackingState
```

## Topics

### Tracking states
- [DeviceAnchor.TrackingState.orientationTracked](deviceanchor/trackingstate-swift.enum/orientationtracked.md)
  The framework is currently only tracking the anchor’s orientation.
- [DeviceAnchor.TrackingState.tracked](deviceanchor/trackingstate-swift.enum/tracked.md)
  The framework is currently tracking both the anchor’s position and its orientation.
- [DeviceAnchor.TrackingState.untracked](deviceanchor/trackingstate-swift.enum/untracked.md)
  The framework isn’t tracking this anchor.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var originFromAnchorTransform: simd_float4x4](deviceanchor/originfromanchortransform.md)
  The transform from the device to the origin coordinate system.
- [var trackingState: DeviceAnchor.TrackingState](deviceanchor/trackingstate-swift.property.md)
  Tracking state of this anchor
- [var isTracked: Bool](deviceanchor/istracked.md)
  A Boolean value that indicates whether ARKit is tracking the device.
- [var description: String](deviceanchor/description.md)
  A textual representation of this anchor.
- [var id: UUID](deviceanchor/id.md)
  The unique identifier of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/deviceanchor/trackingstate-swift.enum)*