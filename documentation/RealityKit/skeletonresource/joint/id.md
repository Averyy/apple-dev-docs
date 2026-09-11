# id

**Framework**: RealityKit  
**Kind**: property

The identifier of the joint, automatically derived from the joint name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var id: String { get }
```

## See Also

- [var restPoseTransform: Transform](skeletonresource/joint/restposetransform.md)
  The rest pose transform of the joint. Defines position, rotation, and scale relative to the parent joint in local space. Used as the reference pose for all animations and deformations.
- [let children: [SkeletonResource.Joint]](skeletonresource/joint/children.md)
  The child joints of this joint. All children must have unique names within the same parent. `JointBuilder` preserves the order children are declared in the closure body, so iteration over `children` is deterministic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/joint/id)*