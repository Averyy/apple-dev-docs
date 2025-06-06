# SpatialTrackingSession.Configuration.AnchorCapability

**Framework**: RealityKit  
**Kind**: struct

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

### Operators
- [static func == (SpatialTrackingSession.Configuration.AnchorCapability, SpatialTrackingSession.Configuration.AnchorCapability) -> Bool](spatialtrackingsession/configuration/anchorcapability/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var debugDescription: String](spatialtrackingsession/configuration/anchorcapability/debugdescription.md)
  A human-readable description of the anchor capability.
- [var hashValue: Int](spatialtrackingsession/configuration/anchorcapability/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](spatialtrackingsession/configuration/anchorcapability/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let body: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/body.md)
  The anchor capability that enables body tracking.
- [static let camera: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/camera.md)
  The anchor capability that enables camera anchoring.
- [static let face: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/face.md)
  The anchor capability that enables face tracking.
- [static let hand: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/hand.md)
  The anchor capability that enables hand tracking.
- [static let image: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/image.md)
  The anchor capability that enables image tracking.
- [static let object: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/object.md)
  The anchor capability that enables object tracking.
- [static let plane: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/plane.md)
  The anchor capability that enables plane detection.
- [static let world: SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability/world.md)
  The anchor capability that enables world tracking.
### Default Implementations
- [CustomStringConvertible Implementations](spatialtrackingsession/configuration/anchorcapability/customstringconvertible-implementations.md)
- [Equatable Implementations](spatialtrackingsession/configuration/anchorcapability/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](spatialtrackingsession/configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors can use scene unerstanding data for.
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](spatialtrackingsession/unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/anchorcapability)*