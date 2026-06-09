# init(named:rootJoint:animationEvaluation:)

**Framework**: RealityKit  
**Kind**: init

Creates a skeleton resource with the specified name, joint hierarchy, and animation-evaluation data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(named name: String, rootJoint: SkeletonResource.Joint, animationEvaluation: SkeletonResource.AnimationEvaluation = .init()) throws
```

#### Discussion

> **Note**: If the joint hierarchy contains invalid data, or if the underlying resource cannot be created.

## Parameters

- `name`: A unique identifier for the skeleton, used by the animation runtime to link animation clips and retargeting configurations to this skeleton.
- `rootJoint`: The root joint of the skeleton hierarchy.
- `animationEvaluation`: Additional animation-related skeletal data to bake into the resource. Defaults to empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/init(named:rootjoint:animationevaluation:))*