# SkeletonResource.JointBuilder

**Framework**: RealityKit  
**Kind**: struct

A result builder for declaratively constructing the children of a joint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct JointBuilder
```

#### Overview

Inside the `Joint(_:restPoseTransform:children:)` closure, you can write any mix of:

- **`Joint` literals** — each becomes one child of the parent joint. ```swift
try Joint("root") {
    try Joint("spine")
    try Joint("hip")
}
// root.children == [spine, hip]
```
- **`[Joint]` values** — each element becomes a child of the parent joint, in array order, alongside any other declarations in the same closure body. Use this when the children are produced from runtime data (e.g. mapped from a flat array) rather than spelled out as literals. ```swift
let kids: [Joint] = ...
try Joint("root") {
    kids   // every element of kids becomes a child of root
}
```

Both forms can be mixed freely. Each `Joint` in any array can itself be a fully built subtree.

## Topics

### Building joints
- [static func buildBlock([SkeletonResource.Joint]...) -> [SkeletonResource.Joint]](skeletonresource/jointbuilder/buildblock(_:).md)
  Combines all joints declared in the closure body into the parent’s `children`.
### Type Methods
- [static buildExpression(_:)](skeletonresource/jointbuilder/buildexpression(_:).md)
  Treats a single `Joint` value in the closure body as one child of the parent.

## See Also

- [var rootJoint: SkeletonResource.Joint](skeletonresource/rootjoint.md)
  The root joint of the skeleton hierarchy.
- [SkeletonResource.Joint](skeletonresource/joint.md)
  Describes a single joint of a `Skeleton`


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/jointbuilder)*