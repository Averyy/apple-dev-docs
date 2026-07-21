# children

**Framework**: RealityKit  
**Kind**: property

The child joints of this joint. All children must have unique names within the same parent. `JointBuilder` preserves the order children are declared in the closure body, so iteration over `children` is deterministic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let children: [SkeletonResource.Joint]
```

## See Also

- [var id: String](skeletonresource/joint/id.md)
  The identifier of the joint, automatically derived from the joint name.
- [var restPoseTransform: Transform](skeletonresource/joint/restposetransform.md)
  The rest pose transform of the joint. Defines position, rotation, and scale relative to the parent joint in local space. Used as the reference pose for all animations and deformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/joint/children)*