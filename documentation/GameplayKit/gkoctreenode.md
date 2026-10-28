# GKOctreeNode

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

A helper class for managing the objects you organize in an octree.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKOctreeNode
```

```objc
@interface GKOctreeNode : NSObject
```

## Overview

You don’t create instances of this class directly; instead, a [`GKOctree`](./gkoctree.md) object provides you with a [`GKOctreeNode`](./gkoctreenode.md) instance when you add an element to a tree. If you plan to remove elements from the tree, keep references to the corresponding nodes so you can use the [`remove(_:using:)`](./gkoctree/remove%28_,using%29.md) method for better performance.

## Topics

### Examining a Node
- [var box: GKBox](./gkoctreenode/box.md)
  The axis-aligned bounding box represented by the node.

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
- [class GKRTree](./gkrtree.md)
  A data structure that adaptively organizes objects based on their locations in a two-dimensional space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctreenode)*