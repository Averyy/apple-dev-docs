# ARSkeleton3D

**Framework**: ARKit  
**Kind**: class

The skeleton of a human body that ARKit tracks in 3D space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSkeleton3D
```

#### Overview

An [`ARBodyAnchor`](arbodyanchor.md) contains one instance of this [`ARSkeleton`](arskeleton.md) subclass to provide its joint positions in 3D space. The [`jointLocalTransforms`](arskeleton3d/jointlocaltransforms-1m5a1.md) property describes a joint’s 3D offset from its parent joint. The [`jointModelTransforms`](arskeleton3d/jointmodeltransforms-dno4.md) property describes a joint’s 3D offset from the body anchor’s [`transform`](aranchor/transform.md).

## Topics

### Getting a Joint’s Pose
- [var jointLocalTransforms: [simd_float4x4]](arskeleton3d/jointlocaltransforms-66gbm.md)
  The local space transforms for each joint.
- [var jointModelTransforms: [simd_float4x4]](arskeleton3d/jointmodeltransforms-i6yu.md)
  The model space transforms for each joint.
- [func localTransform(for: ARSkeleton.JointName) -> simd_float4x4?](arskeleton3d/localtransform(for:).md)
  Returns the local transform for a joint with a given name.
- [func modelTransform(for: ARSkeleton.JointName) -> simd_float4x4?](arskeleton3d/modeltransform(for:).md)
  Returns the model transform for a joint with a given name.

## Relationships

### Inherits From
- [ARSkeleton](arskeleton.md)
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
- [class ARSkeleton2D](arskeleton2d.md)
  An object that describes the locations of a body’s joints in the camera feed.
- [class ARSkeleton](arskeleton.md)
  The interface for the skeleton of a tracked body.
- [class ARSkeletonDefinition](arskeletondefinition.md)
  The hierarchy of joints and their names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d)*