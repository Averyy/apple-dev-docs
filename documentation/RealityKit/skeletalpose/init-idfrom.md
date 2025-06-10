# init(id:from:)

**Framework**: RealityKit  
**Kind**: init

Creates a skeletal pose from the rest pose of the model skeleton.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(id: SkeletalPose.ID, from skeleton: MeshResource.Skeleton)
```

## Parameters

- `id`: The unique name of the pose.
- `skeleton`: The skeleton to extract the joint names and rest pose transformations from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose/init(id:from:))*