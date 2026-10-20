# SpatialTrackingSession.Configuration.AnchorCapability

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type that defines various anchor tracking capabilities.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct AnchorCapability
```

## Topics

### Instance Properties
- [var debugDescription: String](./anchorcapability/debugdescription.md)
  A human-readable description of the anchor capability.
### Type Properties
- [static let accessory: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/accessory.md)
  The anchor capability that enables accessory tracking.
- [static let body: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/body.md)
  The anchor capability that enables body tracking.
- [static let camera: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/camera.md)
  The anchor capability that enables camera anchoring.
- [static let face: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/face.md)
  The anchor capability that enables face tracking.
- [static let hand: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/hand.md)
  The anchor capability that enables hand tracking.
- [static let image: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/image.md)
  The anchor capability that enables image tracking.
- [static let object: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/object.md)
  The anchor capability that enables object tracking.
- [static let plane: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/plane.md)
  The anchor capability that enables plane detection.
- [static let world: SpatialTrackingSession.Configuration.AnchorCapability](./anchorcapability/world.md)
  The anchor capability that enables world tracking.

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
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
- [SpatialTrackingSession.Configuration.Camera](./camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](../unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/anchorcapability)*