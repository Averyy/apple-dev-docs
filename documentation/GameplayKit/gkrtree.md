# GKRTree

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

A data structure that adaptively organizes objects based on their locations in a two-dimensional space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKRTree<ElementType> where ElementType : NSObject
```

```objc
@interface GKRTree : NSObject
```

## Overview

An R-tree manages its structure to optimize for spatial searches—unlike a basic data structure such as an array or dictionary, an R-tree can find all elements occupying a specific position or region very quickly. Additionally, R-trees adapt their internal structure as you add and remove elements, increasing the amount of time required to perform those operations, but decreasing the time required to search for elements later.

An R-tree partitions the space it describes by calculating the minimum bounding regions that enclose each of the added objects. For example, in [Figure 1](./gkrtree.md#1965706), the numbered shapes are objects added to the tree, and the rectangles marked with letters are the data structure the tree creates to organize them.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-1965706@2x.png)

In this example, the rectangle C is the smallest rectangle that entirely contains objects 1 and 2; the rectangle D is the smallest that contains objects 3, 4, and 5; the rectangle A is the smallest containing all the objects in rectangles C and D; and so on. The R-tree automatically creates these divisions in a way that keeps the tree balanced—that is, so that no branch of the tree contains significantly more objects or sub-branches than any other branch—so that searches for objects in the tree require a uniformly minimal amount of processing.

R-trees can be useful for many tasks in game design. For example:

- Deciding which game characters are close enough to each other for interaction
- Deciding which portions of a large game world need to be processed at a given time
- Finding out which other objects are entirely contained within the region occupied by a certain object

The [`GKRTree`](./gkrtree.md) class is one of three spatial partitioning data structures that GameplayKit provides. See these other classes for other tasks:

- The [`GKOctree`](./gkoctree.md) class provides the three-dimensional equivalent of a quadtree. Use an octree when you need to organize objects in 3D space.
- The `GKQuadTree` class provides a different algorithm for two-dimensional spatial indexing. Quadtrees and R-trees have different performance tradeoffs for different tasks: quadtrees can be faster when objects are more uniformly distributed in space or when their positions change frequently, and R-trees can be faster when searching for all objects in a given region.

## Topics

### Creating an R-Tree
- [init(maxNumberOfChildren: Int)](./gkrtree/init%28maxnumberofchildren%29.md)
  Initializes a new R-tree object.
- [+ treeWithMaxNumberOfChildren:](./gkrtree/treewithmaxnumberofchildren_.md)
  Creates a new R-tree object.
### Adding and Removing Elements
- [func addElement(ElementType, boundingRectMin: vector_float2, boundingRectMax: vector_float2, splitStrategy: GKRTreeSplitStrategy)](./gkrtree/addelement%28_,boundingrectmin,boundingrectmax,splitstrategy%29.md)
  Adds the specified object to the tree.
- [func removeElement(ElementType, boundingRectMin: vector_float2, boundingRectMax: vector_float2)](./gkrtree/removeelement%28_,boundingrectmin,boundingrectmax%29.md)
  Removes the specified object from the tree.
### Searching for Elements
- [func elements(inBoundingRectMin: vector_float2, rectMax: vector_float2) -> [ElementType]](./gkrtree/elements%28inboundingrectmin,rectmax%29.md)
  Searches the tree and returns all elements found within the specified bounding region.
- [var queryReserve: Int](./gkrtree/queryreserve.md)
  The number of elements to reserve space for when searching.
### Constants
- [enum GKRTreeSplitStrategy](./gkrtreesplitstrategy.md)
  Options that control how a tree balances its internal structure when adding elements, used with the [`addElement(_:boundingRectMin:boundingRectMax:splitStrategy:)`](./gkrtree/addelement%28_,boundingrectmin,boundingrectmax,splitstrategy%29.md) method.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Spatial Partitioning
- [class GKQuadtree](./gkquadtree.md)
  A data structure for organizing objects based on their locations in a two-dimensional space.
- [class GKQuadtreeNode](./gkquadtreenode.md)
  A helper class for managing the objects you organize in a quadtree.
- [class GKOctree](./gkoctree.md)
  A data structure for organizing objects based on their locations in a three-dimensional space.
- [class GKOctreeNode](./gkoctreenode.md)
  A helper class for managing the objects you organize in an octree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrtree)*