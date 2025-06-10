# WorldAnchor

**Framework**: ARKit  
**Kind**: struct

A fixed location in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct WorldAnchor
```

#### Overview

ARKit persists world anchor UUIDs and transforms across multiple runs of your app. For more information, see [`Tracking specific points in world space`](https://developer.apple.com/documentation/visionOS/tracking-points-in-world-space).

## Topics

### Creating a world anchor
- [init(originFromAnchorTransform: simd_float4x4)](worldanchor/init(originfromanchortransform:).md)
  Creates a world anchor from a position and orientation in world space.
### Identifying a world anchor
- [var id: UUID](worldanchor/id.md)
  The unique identifier of this anchor.
### Inspecting a world anchor
- [var originFromAnchorTransform: simd_float4x4](worldanchor/originfromanchortransform.md)
  The position and orientation of a world anchor.
- [var isTracked: Bool](worldanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking a world anchor.
- [var description: String](worldanchor/description.md)
  A textual representation of this anchor.
### Initializers
- [init(originFromAnchorTransform: simd_float4x4, sharedWithNearbyParticipants: Bool)](worldanchor/init(originfromanchortransform:sharedwithnearbyparticipants:).md)
  Initialize a world anchor with a transform and indicate if it should be shared with nearby participants.
### Instance Properties
- [var isSharedWithNearbyParticipants: Bool](worldanchor/issharedwithnearbyparticipants.md)
  Check if a world anchor is shared with nearby participants.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)

## See Also

- [Tracking specific points in world space](../visionOS/tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [class WorldTrackingProvider](worldtrackingprovider.md)
  A source of live data about the device pose and anchors in a person’s surroundings.
- [struct DeviceAnchor](deviceanchor.md)
  The position and orientation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldanchor)*