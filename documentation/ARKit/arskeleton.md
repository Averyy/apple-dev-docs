# ARSkeleton

**Framework**: ARKit  
**Kind**: class

The interface for the skeleton of a tracked body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSkeleton
```

#### Overview

As a collection of joints, this protocol describes the state of a human body whose movements ARKit can track.

The [`ARSkeleton3D`](arskeleton3d.md) subclass provides you with the position of a tracked body’s joints in 3D space, specifically with its [`jointLocalTransforms`](arskeleton3d/jointlocaltransforms-1m5a1.md) and [`jointModelTransforms`](arskeleton3d/jointmodeltransforms-dno4.md) properties.

The [`ARSkeleton2D`](arskeleton2d.md) subclass provides you with the position of a tracked body’s joints in 2D space, by way of its [`jointLandmarks`](arskeleton2d/jointlandmarks-3en0x.md) property.

## Topics

### Getting Joint Information
- [var definition: ARSkeletonDefinition](arskeleton/definition.md)
  The particular configuration of joints that define a body’s current state.
- [func isJointTracked(Int) -> Bool](arskeleton/isjointtracked(_:).md)
  Tells you whether ARKit tracks a joint at a particular index.
- [ARSkeleton.JointName](arskeleton/jointname.md)
  A name identifier for a joint.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ARSkeleton2D](arskeleton2d.md)
- [ARSkeleton3D](arskeleton3d.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [class ARSkeleton3D](arskeleton3d.md)
  The skeleton of a human body that ARKit tracks in 3D space.
- [class ARSkeleton2D](arskeleton2d.md)
  An object that describes the locations of a body’s joints in the camera feed.
- [class ARSkeletonDefinition](arskeletondefinition.md)
  The hierarchy of joints and their names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton)*