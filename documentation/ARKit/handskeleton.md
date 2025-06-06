# HandSkeleton

**Framework**: ARKit  
**Kind**: struct

A collection of joints in a hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct HandSkeleton
```

## Topics

### Retrieving specific hand joints
- [func joint(HandSkeleton.JointName) -> HandSkeleton.Joint](handskeleton/joint(_:).md)
  Retrieves a hand joint based on the joint name you specify.
- [HandSkeleton.Joint](handskeleton/joint.md)
  The name and position of an individual hand joint.
- [HandSkeleton.JointName](handskeleton/jointname.md)
  The names of different hand joints.
### Inspecting hand skeletons
- [var allJoints: [HandSkeleton.Joint]](handskeleton/alljoints.md)
  All of the joints in a hand skeleton.
- [static var neutralPose: HandSkeleton](handskeleton/neutralpose.md)
  A hand pose that you can use as a reference.
- [var description: String](handskeleton/description.md)
  A textual representation of this Skeleton.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [class HandTrackingProvider](handtrackingprovider.md)
  A source of live data about the position of a person’s hands and hand joints.
- [struct HandAnchor](handanchor.md)
  A hand’s position in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton)*