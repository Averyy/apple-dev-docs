# SpatialTrackingSession.Configuration

**Framework**: RealityKit  
**Kind**: struct

A type for configuring the spatial tracking session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Configuration
```

## Mentions

- [Implementing scene understanding and reconstruction in your RealityKit app](realitykit-scene-understanding.md)

## Topics

### Structures
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
### Initializers
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>)](spatialtrackingsession/configuration/init(tracking:).md)
  Creates a configuration with a set of anchor capabilities.
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>, sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>)](spatialtrackingsession/configuration/init(tracking:sceneunderstanding:).md)
  Creates a configuration with a set of anchor capabilities and scene understanding capabilities.
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>, sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>, camera: SpatialTrackingSession.Configuration.Camera)](spatialtrackingsession/configuration/init(tracking:sceneunderstanding:camera:).md)
  Creates a configuration with anchor capabilities, scene-understanding capabilities, and camera feeds.
### Instance Properties
- [var debugDescription: String](spatialtrackingsession/configuration/debugdescription.md)
  A human-readable description of the configuration.
### Instance Methods
- [func arConfiguration() -> ARConfiguration?](spatialtrackingsession/configuration/arconfiguration.md)
- [func supportedConfiguration() -> SpatialTrackingSession.Configuration](spatialtrackingsession/configuration/supportedconfiguration.md)
### Enumerations
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](spatialtrackingsession/unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration)*