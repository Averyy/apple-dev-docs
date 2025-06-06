# add(_:at:)

**Framework**: GameplayKit  
**Kind**: method

Adds an object to the tree corresponding to the specified point in 3D space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ element: ElementType, at point: vector_float3) -> GKOctreeNode
```

#### Return Value

The tree node containing the newly added object.

#### Discussion

The [`GKOctree`](gkoctree.md) class automatically creates nodes to manage the objects you add to the tree. If you expect to remove an element you’ve added, keep a reference to the node this method returns so you can use the [`remove(_:using:)`](gkoctree/remove(_:using:).md) method to remove that object quickly.

## Parameters

- `element`: The object to add to the tree.
- `point`: The point in 2D space to which the object corresponds.

## See Also

- [func add(ElementType, in: GKBox) -> GKOctreeNode](gkoctree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType, using: GKOctreeNode) -> Bool](gkoctree/remove(_:using:).md)
  Removes the specified object from the tree, using a reference to its containing node.
- [func remove(ElementType) -> Bool](gkoctree/remove(_:).md)
  Searches for the specified object and removes it from the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/add(_:at:))*