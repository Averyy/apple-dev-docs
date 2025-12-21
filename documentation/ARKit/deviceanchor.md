# DeviceAnchor

**Framework**: ARKit  
**Kind**: struct

The position and orientation of Apple Vision Pro.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct DeviceAnchor
```

#### Overview

You create a device anchor by starting an [`ARKitSession`](arkitsession.md) with a [`WorldTrackingProvider`](worldtrackingprovider.md) and calling its [`queryDeviceAnchor(atTimestamp:)`](worldtrackingprovider/querydeviceanchor(attimestamp:).md) method.

## Topics

### Inspecting a device anchor
- [var originFromAnchorTransform: simd_float4x4](deviceanchor/originfromanchortransform.md)
  The transform from the device to the origin coordinate system.
- [var trackingState: DeviceAnchor.TrackingState](deviceanchor/trackingstate-swift.property.md)
  Tracking state of this anchor
- [DeviceAnchor.TrackingState](deviceanchor/trackingstate-swift.enum.md)
  Values that describe the tracking state of a device anchor.
- [var isTracked: Bool](deviceanchor/istracked.md)
  A Boolean value that indicates whether ARKit is tracking the device.
- [var description: String](deviceanchor/description.md)
  A textual representation of this anchor.
- [var id: UUID](deviceanchor/id.md)
  The unique identifier of this anchor.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)

## See Also

- [Tracking specific points in world space](../visionOS/tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [class WorldTrackingProvider](worldtrackingprovider.md)
  A source of live data about the device pose and anchors in a person’s surroundings.
- [struct WorldAnchor](worldanchor.md)
  A fixed location in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/deviceanchor)*