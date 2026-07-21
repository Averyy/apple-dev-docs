# rootJoint

**Framework**: RealityKit  
**Kind**: property

The root joint of the skeleton hierarchy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var rootJoint: SkeletonResource.Joint { get }
```

#### Discussion

> **Note**: Each access walks the resource and rebuilds the entire `Joint` tree. Bind the value to a `let` once when iterating or recursing over the hierarchy rather than re-reading the property in a loop.

## See Also

- [SkeletonResource.Joint](skeletonresource/joint.md)
  Describes a single joint of a `Skeleton`
- [SkeletonResource.JointBuilder](skeletonresource/jointbuilder.md)
  A result builder for declaratively constructing the children of a joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/rootjoint)*