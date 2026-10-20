# SpatialTrackingSession.UnavailableCapabilities

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type that contains the unavailable capabilities of the current spatial tracking session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct UnavailableCapabilities
```

## Topics

### Initializers
- [init()](./unavailablecapabilities/init%28%29.md)
  Creates an unavailable capabilities instance.
### Instance Properties
- [var anchor: Set<SpatialTrackingSession.Configuration.AnchorCapability>](./unavailablecapabilities/anchor.md)
  A type that contains all unavailable anchor capabilities.
- [var debugDescription: String](./unavailablecapabilities/debugdescription.md)
- [var missingAuthorizations: Set<ARKitSession.AuthorizationType>](./unavailablecapabilities/missingauthorizations.md)
  The set of requested ARKit authorizations that the user doesn’t approve.
- [var missingCameraAuthorization: Bool?](./unavailablecapabilities/missingcameraauthorization.md)
  Whether the person using the device approves the camera authorization or not.
- [var sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>](./unavailablecapabilities/sceneunderstanding.md)
  A type that contains all unavailable scene-understanding capabilities.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Spatial tracking
- [class SpatialTrackingSession](../spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](./configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](./configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](./configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
- [SpatialTrackingSession.Configuration.Camera](./configuration/camera.md)
  Defines the camera feed the RealityView renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/unavailablecapabilities)*