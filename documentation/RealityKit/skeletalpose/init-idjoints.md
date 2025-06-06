# init(id:joints:)

**Framework**: RealityKit  
**Kind**: init

Creates a pose for the joint name and transformation pairs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(id: SkeletalPose.ID, joints: [(String, JointTransforms.Element)])
```

## Parameters

- `id`: The unique name of the pose.
- `joints`: An array of tuples, each containing a name and its corresponding transformation, arranged in any order of your choosing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose/init(id:joints:))*