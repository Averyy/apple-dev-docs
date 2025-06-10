# MeshSkeletonCollection

**Framework**: RealityKit  
**Kind**: struct

An object that holds a collection of skeletons used by a mesh resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct MeshSkeletonCollection
```

## Topics

### Initializers
- [init()](meshskeletoncollection/init.md)
- [init(_:)](meshskeletoncollection/init(_:).md)
### Instance Properties
- [var count: Int](meshskeletoncollection/count.md)
  Number of skeletons.
- [var isEmpty: Bool](meshskeletoncollection/isempty.md)
  True if there are no skeletons.
### Instance Methods
- [func insert(_:)](meshskeletoncollection/insert(_:).md)
  Add a new skeleton to the container. Returns true if added. Returns false if it already exists.
- [func remove(id:)](meshskeletoncollection/remove(id:).md)
  Remove a skeleton by id.
- [func removeAll()](meshskeletoncollection/removeall.md)
  Remove all the skeletons.
- [func update(_:)](meshskeletoncollection/update(_:).md)
  Update an existing skeleton. The old instance is returned.
### Subscripts
- [subscript(_:)](meshskeletoncollection/subscript(_:).md)
  Read a skeleton given its id.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshskeletoncollection)*