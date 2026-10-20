# SkeletalPoseSet

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of named skeletal poses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct SkeletalPoseSet
```

## Topics

### Initializers
- [init()](./skeletalposeset/init%28%29.md)
  Creates an empty collection.
### Instance Properties
- [var count: Int](./skeletalposeset/count.md)
  The number of elements in the collection.
- [var `default`: SkeletalPoseSet.Element?](./skeletalposeset/default.md)
  Accesses the first skeletal pose.
- [var isEmpty: Bool](./skeletalposeset/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(SkeletalPose.ID) -> Bool](./skeletalposeset/contains%28_%29.md)
  Checks if the set contains a pose with the given name.
- [func index(of: SkeletalPose.ID) -> SkeletalPoseSet.Index?](./skeletalposeset/index%28of%29.md)
  Returns the index where the specified pose appears in the collection.
- [func set(SkeletalPoseSet.Element) -> SkeletalPoseSet.Element?](./skeletalposeset/set%28_%29.md)
  Updates a pose in the set based on its name. If pose with this ID does not exist, does nothing.
### Default Implementations
- [Collection Implementations](./skeletalposeset/collection-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Skeletons
- [struct SkeletalPosesComponent](./skeletalposescomponent.md)
  A component that exposes the collection of named animation skeletal poses.
- [struct SkeletalPose](./skeletalpose.md)
  A container that holds the position and orientation of each joint in a single animation skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset)*