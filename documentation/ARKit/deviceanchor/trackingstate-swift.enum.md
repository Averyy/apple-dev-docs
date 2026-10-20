# DeviceAnchor.TrackingState

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe the tracking state of a device anchor.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum TrackingState
```

## Topics

### Tracking states
- [DeviceAnchor.TrackingState.orientationTracked](./trackingstate-swift.enum/orientationtracked.md)
  The framework is currently only tracking the anchor’s orientation.
- [DeviceAnchor.TrackingState.tracked](./trackingstate-swift.enum/tracked.md)
  The framework is currently tracking both the anchor’s position and its orientation.
- [DeviceAnchor.TrackingState.untracked](./trackingstate-swift.enum/untracked.md)
  The framework isn’t tracking this anchor.
### Instance Properties
- [var description: String](./trackingstate-swift.enum/description.md)
  A textual representation of this tracking state.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a device anchor
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the device to the origin coordinate system.
- [var trackingState: DeviceAnchor.TrackingState](./trackingstate-swift.property.md)
  Tracking state of this anchor
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit is tracking the device.
- [var description: String](./description.md)
  A textual representation of this anchor.
- [var id: UUID](./id.md)
  The unique identifier of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/deviceanchor/trackingstate-swift.enum)*