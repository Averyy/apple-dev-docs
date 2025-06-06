# remove(_:)

**Framework**: GameplayKit  
**Kind**: method

Searches for the specified object and removes it from the tree.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ element: ElementType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the object was removed from the tree. [`false`](https://developer.apple.com/documentation/swift/false) if the specified object is not in the tree.

#### Discussion

The tree does not directly reference its elements—octrees are optimized to search for elements based on spatial positions—so this method must exhaustively search the entire tree to find the object to remove. For quicker removal, keep a reference to the [`GKOctreeNode`](gkoctreenode.md) object returned when you add an object to the tree, and call the [`remove(_:using:)`](gkoctree/remove(_:using:).md) method instead.

## Parameters

- `element`: The object to be removed from the tree.

## See Also

- [func add(ElementType, at: vector_float3) -> GKOctreeNode](gkoctree/add(_:at:).md)
  Adds an object to the tree corresponding to the specified point in 3D space.
- [func add(ElementType, in: GKBox) -> GKOctreeNode](gkoctree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType, using: GKOctreeNode) -> Bool](gkoctree/remove(_:using:).md)
  Removes the specified object from the tree, using a reference to its containing node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/remove(_:))*