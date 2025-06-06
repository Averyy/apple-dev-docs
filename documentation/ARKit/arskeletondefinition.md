# ARSkeletonDefinition

**Framework**: ARKit  
**Kind**: class

The hierarchy of joints and their names.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSkeletonDefinition
```

#### Overview

A skeleton definition establishes the relationship of joints that make up a 3D or 2D body’s [`skeleton`](arbody2d/skeleton.md), in which joints connect to other joints to compose a single skeleton in a parent-child hierarchy. Use [`parentIndices`](arskeletondefinition/parentindices-82iw2.md) to identify the hierarchy for a given skeleton definition.

ARKit names particular joints that are crucial to body tracking. You can access named joints by calling [`indexForJointName:`](arskeletondefinition/indexforjointname:.md) and passing in one of the available [`jointNames`](arskeletondefinition/jointnames.md) identifiers.

## Topics

### Locating in the Physical Environment
- [var neutralBodySkeleton3D: ARSkeleton3D?](arskeletondefinition/neutralbodyskeleton3d.md)
  The 3D skeleton in neutral pose.
- [class var defaultBody3D: ARSkeletonDefinition](arskeletondefinition/defaultbody3d.md)
  The default skeleton definition for bodies defined in 3D.
### Locating in Screen Space
- [class var defaultBody2D: ARSkeletonDefinition](arskeletondefinition/defaultbody2d.md)
  The default skeleton definition for bodies defined in 2D.
### Getting Joint Information
- [var jointNames: [String]](arskeletondefinition/jointnames.md)
  A collection of unique joint names.
- [var jointCount: Int](arskeletondefinition/jointcount.md)
  The skeleton’s total number of joints.
- [func index(for: ARSkeleton.JointName) -> Int](arskeletondefinition/index(for:).md)
  Returns the index for a given joint identifier.
- [var parentIndices: [Int]](arskeletondefinition/parentindices-u2u9.md)
  The parent index for each joint.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [class ARSkeleton3D](arskeleton3d.md)
  The skeleton of a human body that ARKit tracks in 3D space.
- [class ARSkeleton2D](arskeleton2d.md)
  An object that describes the locations of a body’s joints in the camera feed.
- [class ARSkeleton](arskeleton.md)
  The interface for the skeleton of a tracked body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition)*