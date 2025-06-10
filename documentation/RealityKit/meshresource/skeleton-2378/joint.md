# MeshResource.Skeleton.Joint

**Framework**: RealityKit  
**Kind**: struct

A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton-2378.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct Joint
```

## Topics

### Initializers
- [init(name:parentIndex:inverseBindPoseMatrix:restPoseTransform:)](meshresource/skeleton-2om5m/joint/init(name:parentindex:inversebindposematrix:restposetransform:).md)
  Creates a single joint in a skeleton.
### Instance Properties
- [var inverseBindPoseMatrix: simd_float4x4](meshresource/skeleton-2378/joint/inversebindposematrix.md)
  A matrix which transforms from the authored pose (the “bind pose”) of the bound model to the local space of this joint.
- [var name: String](meshresource/skeleton-2378/joint/name.md)
  The name of this joint.
- [var parentIndex: Int?](meshresource/skeleton-2378/joint/parentindex.md)
  The index of this joint’s parent, or nil if this joint has no parent.
- [var restPoseTransform: Transform](meshresource/skeleton-2378/joint/restposetransform.md)
  The local transform of this joint in skeleton’s rest pose, specified relative to this joint’s parent (or relative to model space, if this joint has no parent).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton-2378/joint)*