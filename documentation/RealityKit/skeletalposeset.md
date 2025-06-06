# SkeletalPoseSet

**Framework**: RealityKit  
**Kind**: struct

A collection of named skeletal poses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct SkeletalPoseSet
```

## Topics

### Initializers
- [init()](skeletalposeset/init.md)
  Creates an empty collection.
### Instance Properties
- [var count: Int](skeletalposeset/count.md)
  The number of elements in the collection.
- [var `default`: SkeletalPoseSet.Element?](skeletalposeset/default.md)
  Accesses the first skeletal pose.
- [var isEmpty: Bool](skeletalposeset/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(SkeletalPose.ID) -> Bool](skeletalposeset/contains(_:).md)
  Checks if the set contains a pose with the given name.
- [func index(of: SkeletalPose.ID) -> SkeletalPoseSet.Index?](skeletalposeset/index(of:).md)
  Returns the index where the specified pose appears in the collection.
- [func set(SkeletalPoseSet.Element) -> SkeletalPoseSet.Element?](skeletalposeset/set(_:).md)
  Updates a pose in the set based on its name. If pose with this ID does not exist, does nothing.
### Subscripts
- [subscript(SkeletalPose.ID) -> SkeletalPoseSet.Element?](skeletalposeset/subscript(_:)-54jc0.md)
  Accesses the element with the specified identifier.
### Type Aliases
- [SkeletalPoseSet.Element](skeletalposeset/element.md)
  A type representing the sequence’s elements.
### Default Implementations
- [Collection Implementations](skeletalposeset/collection-implementations.md)
- [Sequence Implementations](skeletalposeset/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct SkeletalPosesComponent](skeletalposescomponent.md)
  A component that exposes the collection of named animation skeletal poses.
- [struct SkeletalPose](skeletalpose.md)
  A container that holds the position and orientation of each joint in a single animation skeleton.
- [SkeletalPose.ID](skeletalpose/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [SkeletalPoseSet.Element](skeletalposeset/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset)*