# SpatialTrackingSession.UnavailableCapabilities

**Framework**: RealityKit  
**Kind**: struct

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
- [init()](spatialtrackingsession/unavailablecapabilities/init.md)
  Creates an unavailable capabilities instance.
### Instance Properties
- [var anchor: Set<SpatialTrackingSession.Configuration.AnchorCapability>](spatialtrackingsession/unavailablecapabilities/anchor.md)
  A type that contains all unavailable anchor capabilities.
- [var debugDescription: String](spatialtrackingsession/unavailablecapabilities/debugdescription.md)
- [var missingAuthorizations: Set<ARKitSession.AuthorizationType>](spatialtrackingsession/unavailablecapabilities/missingauthorizations.md)
  The set of requested ARKit authorizations that the user doesn’t approve.
- [var missingCameraAuthorization: Bool?](spatialtrackingsession/unavailablecapabilities/missingcameraauthorization.md)
  Whether the person using the device approves the camera authorization or not.
- [var sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability>](spatialtrackingsession/unavailablecapabilities/sceneunderstanding.md)
  A type that contains all unavailable scene-understanding capabilities.
### Default Implementations
- [CustomStringConvertible Implementations](spatialtrackingsession/unavailablecapabilities/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](spatialtrackingsession/configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors can use scene unerstanding data for.
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/unavailablecapabilities)*