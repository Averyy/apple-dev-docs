# SpatialTrackingSession.Configuration.Camera

**Framework**: RealityKit  
**Kind**: enum

Defines the camera feed the RealityView renders.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Camera
```

## Topics

### Operators
- [static func == (SpatialTrackingSession.Configuration.Camera, SpatialTrackingSession.Configuration.Camera) -> Bool](spatialtrackingsession/configuration/camera/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [SpatialTrackingSession.Configuration.Camera.back](spatialtrackingsession/configuration/camera/back.md)
  The camera on the back of the device.
- [SpatialTrackingSession.Configuration.Camera.front](spatialtrackingsession/configuration/camera/front.md)
  The camera on the front of the device.
### Instance Properties
- [var hashValue: Int](spatialtrackingsession/configuration/camera/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](spatialtrackingsession/configuration/camera/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](spatialtrackingsession/configuration/camera/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](spatialtrackingsession/configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors can use scene unerstanding data for.
- [SpatialTrackingSession.UnavailableCapabilities](spatialtrackingsession/unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/camera)*