# AccessoryAnchor

**Framework**: ARKit  
**Kind**: struct

Represents a tracked accessory.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AccessoryAnchor
```

## Topics

### Instance Properties
- [var accessory: Accessory](accessoryanchor/accessory.md)
  Accessory tracked by this anchor.
- [var angularVelocity: SIMD3<Float>](accessoryanchor/angularvelocity.md)
  Angular velocity of the accessory in the local coordinate system [rad/s].
- [var description: String](accessoryanchor/description.md)
  A textual representation of this anchor.
- [var heldChirality: Accessory.Chirality?](accessoryanchor/heldchirality.md)
  Which hand the accessory is currently held in. Returns nil if the accessory is not held.
- [var id: UUID](accessoryanchor/id.md)
  The unique identifier of this anchor.
- [var isTracked: Bool](accessoryanchor/istracked.md)
  Whether this anchor is currently tracked or not.
- [var originFromAnchorTransform: simd_float4x4](accessoryanchor/originfromanchortransform.md)
  The transform from the accessory anchor to the origin coordinate system.
- [var trackingState: AccessoryAnchor.TrackingState](accessoryanchor/trackingstate-swift.property.md)
  Tracking state of this anchor.
- [var velocity: SIMD3<Float>](accessoryanchor/velocity.md)
  Velocity of the accessory in the local coordinate system [m/s].
### Instance Methods
- [func coordinateSpace(correction: ARKitCoordinateSpace.Correction) -> ARKitCoordinateSpace](accessoryanchor/coordinatespace(correction:).md)
  The anchor coordinate space.
- [func coordinateSpace(for: Accessory.LocationName, correction: ARKitCoordinateSpace.Correction) -> ARKitCoordinateSpace](accessoryanchor/coordinatespace(for:correction:).md)
  The coordinate space of a location on this accessory.
### Enumerations
- [AccessoryAnchor.TrackingState](accessoryanchor/trackingstate-swift.enum.md)
  Tracking state of accessory anchors.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessoryanchor)*