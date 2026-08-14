# SpatialTrackingSession.Configuration.SceneUnderstandingCapability

**Framework**: RealityKit  
**Kind**: struct

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
- [var debugDescription: String](spatialtrackingsession/configuration/sceneunderstandingcapability/debugdescription.md)
  A human-readable description of the scene-understanding capability.
### Type Properties
- [static let collision: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability/collision.md)
  The capability that allows the system to use scene-understanding data for collisions.
- [static let occlusion: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability/occlusion.md)
  The capability that allows the system to use scene-understanding data for occlusion.
- [static let physics: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability/physics.md)
  The capability that allows the system to use scene-understanding data for physics simulation.
- [static let shadow: SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability/shadow.md)
  The capability that allows the system to use scene-understanding data for shadow casting.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](spatialtrackingsession/configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](spatialtrackingsession/unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/sceneunderstandingcapability)*