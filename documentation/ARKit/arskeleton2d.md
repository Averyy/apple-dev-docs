# ARSkeleton2D

**Framework**: ARKit  
**Kind**: class

An object that describes the locations of a body’s joints in the camera feed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSkeleton2D
```

#### Overview

[`ARSkeleton2D`](arskeleton2d.md) provides you with a 2D body’s joints in a flat hierarchy so you can access them efficiently. The joint locations are normalized within the range [0..1] in the coordinate space of the current frame’s camera image, where 0 is the upper left, and 1 is the bottom right.

To access a skeleton’s joints by name, you use [`landmarkForJointNamed:`](arskeleton2d/landmarkforjointnamed:.md). To access a named joint by index (for example, for performance reasons), you query the definition for the named joint index using [`index(for:)`](arskeletondefinition/index(for:).md), then access [`jointLandmarks`](arskeleton2d/jointlandmarks-12vkw.md) using the resulting index.

## Topics

### Getting Joint Landmarks
- [var jointLandmarks: [simd_float2]](arskeleton2d/jointlandmarks-12vkw.md)
  The joint landmarks in normalized coordinates.
- [func landmark(for: ARSkeleton.JointName) -> simd_float2?](arskeleton2d/landmark(for:).md)
  Returns the location of a joint with a given name.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [class ARSkeleton3D](arskeleton3d.md)
  The skeleton of a human body that ARKit tracks in 3D space.
- [class ARSkeleton](arskeleton.md)
  The interface for the skeleton of a tracked body.
- [class ARSkeletonDefinition](arskeletondefinition.md)
  The hierarchy of joints and their names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton2d)*