# GKOctree

**Framework**: GameplayKit  
**Kind**: class

A data structure for organizing objects based on their locations in a three-dimensional space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKOctree<ElementType> where ElementType : NSObject
```

#### Overview

An octree manages its structure to optimize for spatial searches—unlike a basic data structure such as an array or dictionary, an octree can find all elements occupying a specific position or volume very quickly. The octree partitioning strategy divides space into eight octants at each level, as illustrated in [`Figure 1`](gkoctree#1965708.md). When an octant contains more than one object, the tree subdivides that region into eight smaller octants, adding a level to the tree.

![None](https://docs-assets.developer.apple.com/published/7438d4db9a93c3bf5caf8148b6562337/media-1965708%402x.png)

Octrees can be useful for many tasks in game design. For example:

- Deciding which game characters are close enough to each other for interaction
- Deciding which portions of a large game world need to be processed at a given time

The [`GKOctree`](gkoctree.md) class is one of three spatial partitioning data structures that GameplayKit provides, and the only one suited to three-dimensional data. See the `GKQuadTree` class for the two-dimensional analogue of an octree, and the [`GKRTree`](gkrtree.md) class for different ways to organize two-dimensional data.

## Topics

### Creating an Octree
- [init(boundingBox: GKBox, minimumCellSize: Float)](gkoctree/init(boundingbox:minimumcellsize:).md)
  Initializes an octree with the specified dimensions.
### Adding and Removing Elements
- [func add(ElementType, at: vector_float3) -> GKOctreeNode](gkoctree/add(_:at:).md)
  Adds an object to the tree corresponding to the specified point in 3D space.
- [func add(ElementType, in: GKBox) -> GKOctreeNode](gkoctree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType, using: GKOctreeNode) -> Bool](gkoctree/remove(_:using:).md)
  Removes the specified object from the tree, using a reference to its containing node.
- [func remove(ElementType) -> Bool](gkoctree/remove(_:).md)
  Searches for the specified object and removes it from the tree.
### Searching for Elements
- [func elements(at: vector_float3) -> [ElementType]](gkoctree/elements(at:).md)
  Returns all objects whose corresponding locations overlap the specified point.
- [func elements(in: GKBox) -> [ElementType]](gkoctree/elements(in:).md)
  Returns all objects whose corresponding locations overlap the specified volume.
### Constants
- [struct GKBox](gkbox.md)
  The definition of an axis-aligned rectangular bounding volume addressed by the tree.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKQuadtree](gkquadtree.md)
  A data structure for organizing objects based on their locations in a two-dimensional space.
- [class GKQuadtreeNode](gkquadtreenode.md)
  A helper class for managing the objects you organize in a quadtree.
- [class GKOctreeNode](gkoctreenode.md)
  A helper class for managing the objects you organize in an octree.
- [class GKRTree](gkrtree.md)
  A data structure that adaptively organizes objects based on their locations in a two-dimensional space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree)*