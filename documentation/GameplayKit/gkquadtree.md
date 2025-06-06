# GKQuadtree

**Framework**: GameplayKit  
**Kind**: class

A data structure for organizing objects based on their locations in a two-dimensional space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKQuadtree<ElementType> where ElementType : NSObject
```

#### Overview

A quadtree manages its structure to optimize for spatial searches—unlike a basic data structure such as an array or dictionary, a quadtree can find all elements occupying a specific position or region very quickly. The quadtree partitioning strategy divides space into four quadrants at each level, as illustrated in [`Figure 1`](gkquadtree#1965707.md). When a quadrant contains more than one object, the tree subdivides that region into four smaller quadrants, adding a level to the tree.

![None](https://docs-assets.developer.apple.com/published/43b632815a9aac05024873e4495e98c1/media-1965707%402x.png)

Quadtrees can be useful for many tasks in game design. For example:

- Deciding which game characters are close enough to each other for interaction
- Deciding which portions of a large game world need to be processed at a given time

The [`GKQuadtree`](gkquadtree.md) class is one of three spatial partitioning data structures that GameplayKit provides. See these other classes for other tasks:

- The [`GKOctree`](gkoctree.md) class provides the three-dimensional equivalent of a quadtree. Use an octree when you need to organize objects in 3D space.
- The [`GKRTree`](gkrtree.md) class provides a different algorithm for two-dimensional spatial indexing. Quadtrees and R-trees have different performance tradeoffs for different tasks: quadtrees can be faster when objects are more uniformly distributed in space or when their positions change frequently, and R-trees can be faster when searching for all objects in a given region.

## Topics

### Creating a Quadtree
- [init(boundingQuad: GKQuad, minimumCellSize: Float)](gkquadtree/init(boundingquad:minimumcellsize:).md)
  Initializes a quadtree with the specified dimensions.
### Adding and Removing Elements
- [func add(ElementType, at: vector_float2) -> GKQuadtreeNode](gkquadtree/add(_:at:).md)
  Adds an object to the tree corresponding to the specified point in 2D space.
- [func add(ElementType, in: GKQuad) -> GKQuadtreeNode](gkquadtree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified region of 2D space.
- [func remove(ElementType, using: GKQuadtreeNode) -> Bool](gkquadtree/remove(_:using:).md)
  Removes the specified object from the tree, using a reference to its containing node.
- [func remove(ElementType) -> Bool](gkquadtree/remove(_:).md)
  Searches for the specified object and removes it from the tree.
### Searching for Elements
- [func elements(at: vector_float2) -> [ElementType]](gkquadtree/elements(at:).md)
  Returns all objects whose corresponding locations overlap the specified point.
- [func elements(in: GKQuad) -> [ElementType]](gkquadtree/elements(in:).md)
  Returns all objects whose corresponding locations overlap the specified region.
### Constants
- [struct GKQuad](gkquad.md)
  The definition of an axis-aligned rectangle addressed by the tree.

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

- [class GKQuadtreeNode](gkquadtreenode.md)
  A helper class for managing the objects you organize in a quadtree.
- [class GKOctree](gkoctree.md)
  A data structure for organizing objects based on their locations in a three-dimensional space.
- [class GKOctreeNode](gkoctreenode.md)
  A helper class for managing the objects you organize in an octree.
- [class GKRTree](gkrtree.md)
  A data structure that adaptively organizes objects based on their locations in a two-dimensional space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtree)*