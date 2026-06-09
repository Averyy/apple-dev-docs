# AccessoryAnchor

**Framework**: ARKit  
**Kind**: struct

Represents a tracked accessory.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct AccessoryAnchor
```

## Topics

### Operators
- [static func == (AccessoryAnchor, AccessoryAnchor) -> Bool](accessoryanchor/==(_:_:).md)
  Returns a Boolean value indicating whether two accessory anchors are equal.
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
  The anchor’s coordinate space.
- [func coordinateSpace(for: Accessory.LocationName, correction: ARKitCoordinateSpace.Correction) -> ARKitCoordinateSpace](accessoryanchor/coordinatespace(for:correction:).md)
  The coordinate space of a location on this accessory.
### Enumerations
- [AccessoryAnchor.TrackingState](accessoryanchor/trackingstate-swift.enum.md)
  Tracking state of accessory anchors.

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](arkitcoordinatespaceproviding.md)
- [Anchor](anchor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)

## See Also

- [Preparing spatial accessories for tracking in your visionOS app](preparing-spatial-accessories-for-tracking-in-your-visionos-app.md)
  Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.
- [Working with generic spatial accessories](../visionOS/working-with-generic-spatial-accessories.md)
  Use generic spatial accessories to track purpose-built devices in your visionOS app.
- [class AccessoryTrackingProvider](accessorytrackingprovider.md)
  Provides the real time position of accessories in the user’s environment.
- [struct Accessory](accessory.md)
  Represents an accessory to be tracked.
- [Tracking accessories in volumetric windows](tracking-accessories-in-volumetric-windows.md)
  Translate the position and velocity of tracked handheld accessories to throw virtual balls at a stack of cans.
- [Tracking a handheld accessory as a virtual sculpting tool](tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.md)
  Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessoryanchor)*