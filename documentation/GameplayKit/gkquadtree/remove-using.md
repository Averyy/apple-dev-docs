# remove(_:using:)

**Framework**: GameplayKit  
**Kind**: method

Removes the specified object from the tree, using a reference to its containing node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ data: ElementType, using node: GKQuadtreeNode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the object was removed from the tree. [`false`](https://developer.apple.com/documentation/swift/false) if the specified object or node is not in the tree.

#### Discussion

By referencing the node that contains the object to remove, this method can quickly remove an object from the tree without needing to perform an exhaustive search. To make use of this performance optimization, keep a reference to the node returned when you add elements with the [`add(_:at:)`](gkquadtree/add(_:at:).md) or [`add(_:in:)`](gkquadtree/add(_:in:).md) methods.

## Parameters

- `data`: The object to be removed from the tree.
- `node`: The node in the tree containing the object.

## See Also

- [func add(ElementType, at: vector_float2) -> GKQuadtreeNode](gkquadtree/add(_:at:).md)
  Adds an object to the tree corresponding to the specified point in 2D space.
- [func add(ElementType, in: GKQuad) -> GKQuadtreeNode](gkquadtree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified region of 2D space.
- [func remove(ElementType) -> Bool](gkquadtree/remove(_:).md)
  Searches for the specified object and removes it from the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtree/remove(_:using:))*