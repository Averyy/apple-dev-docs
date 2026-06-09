# HandAnchor

**Framework**: ARKit  
**Kind**: struct

A hand’s position in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct HandAnchor
```

## Topics

### Getting hand information
- [var originFromAnchorTransform: simd_float4x4](handanchor/originfromanchortransform.md)
  The location and orientation of a hand in world space.
- [var handSkeleton: HandSkeleton?](handanchor/handskeleton.md)
  The current position and orientation of joints on a hand.
- [var chirality: HandAnchor.Chirality](handanchor/chirality-swift.property.md)
  The chirality of this hand.
- [HandAnchor.Chirality](handanchor/chirality-swift.enum.md)
  A value that indicates a left or right hand.
- [var isTracked: Bool](handanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this hand.
- [var description: String](handanchor/description.md)
  A textual representation of this anchor.
### Identifying hand anchors
- [var id: UUID](handanchor/id.md)
  The unique identifier of this anchor.
### Instance Properties
- [var fidelity: HandAnchor.Fidelity](handanchor/fidelity-swift.property.md)
  The fidelity of this hand.
### Enumerations
- [HandAnchor.Fidelity](handanchor/fidelity-swift.enum.md)
  Enumeration to distinguish hand fidelity
### Default Implementations
- [ARKitCoordinateSpaceProviding Implementations](handanchor/arkitcoordinatespaceproviding-implementations.md)
- [Equatable Implementations](handanchor/equatable-implementations.md)

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

- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [Creating a 3D painting space](../visionOS/creating-a-painting-space-in-visionos.md)
  Implement a painting canvas entity, and update its mesh to represent a stroke.
- [Tracking and visualizing hand movement](../visionOS/tracking-and-visualizing-hand-movement.md)
  Use hand-tracking anchors to display a visual representation of hand transforms in visionOS.
- [class HandTrackingProvider](handtrackingprovider.md)
  A source of live data about the position of a person’s hands and hand joints.
- [struct HandSkeleton](handskeleton.md)
  A collection of joints in a hand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor)*