# init(_:restPoseTransform:children:)

**Framework**: RealityKit  
**Kind**: init

Creates a joint with the provided name, rest pose transform, and optional children.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ name: String, restPoseTransform: Transform = .identity, @SkeletonResource.JointBuilder children: () throws -> [SkeletonResource.Joint] = { [] }) throws
```

#### Discussion

> **Note**: If any children share the same name.

## Parameters

- `name`: The unique name of the new joint
- `restPoseTransform`: The local space transformation relative to the parent joint
- `children`: A result builder closure that returns child joints


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/joint/init(_:restposetransform:children:))*