# SpatialTrackingSession.Configuration.SceneUnderstandingCapability

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines how system behaviors use scene understanding.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```swift
struct SceneUnderstandingCapability
```

## Topics

### Instance Properties
- [var debugDescription: String](./sceneunderstandingcapability/debugdescription.md)
  A human-readable description of the scene-understanding capability.
### Type Properties
- [static let collision: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./sceneunderstandingcapability/collision.md)
  The capability that allows the system to use scene-understanding data for collisions.
- [static let occlusion: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./sceneunderstandingcapability/occlusion.md)
  The capability that allows the system to use scene-understanding data for occlusion.
- [static let physics: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./sceneunderstandingcapability/physics.md)
  The capability that allows the system to use scene-understanding data for physics simulation.
- [static let shadow: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./sceneunderstandingcapability/shadow.md)
  The capability that allows the system to use scene-understanding data for shadow casting.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Spatial tracking
- [class SpatialTrackingSession](../../spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](../configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.Camera](./camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](../unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/sceneunderstandingcapability)*