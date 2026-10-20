# SpatialTrackingSession.Configuration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type for configuring the spatial tracking session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Structures
- [SpatialTrackingSession.Configuration.AnchorCapability](./configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
### Initializers
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>)](./configuration/init%28tracking%29.md)
  Creates a configuration with a set of anchor capabilities.
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>, sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>)](./configuration/init%28tracking,sceneunderstanding%29.md)
  Creates a configuration with a set of anchor capabilities and scene understanding capabilities.
- [init(tracking: Set<SpatialTrackingSession.Configuration.AnchorCapability>, sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>, camera: SpatialTrackingSession.Configuration.Camera)](./configuration/init%28tracking,sceneunderstanding,camera%29.md)
  Creates a configuration with anchor capabilities, scene-understanding capabilities, and camera feeds.
### Instance Properties
- [var debugDescription: String](./configuration/debugdescription.md)
  A human-readable description of the configuration.
### Instance Methods
- [func arConfiguration() -> ARConfiguration?](./configuration/arconfiguration%28%29.md)
- [func supportedConfiguration() -> SpatialTrackingSession.Configuration](./configuration/supportedconfiguration%28%29.md)
### Enumerations
- [SpatialTrackingSession.Configuration.Camera](./configuration/camera.md)
  Defines the camera feed the RealityView renders.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Spatial tracking
- [class SpatialTrackingSession](../spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration.AnchorCapability](./configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
- [SpatialTrackingSession.Configuration.Camera](./configuration/camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](./unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration)*