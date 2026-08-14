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
func remove(_ element: ElementType, using node: GKOctreeNode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the object was removed from the tree. [`false`](https://developer.apple.com/documentation/swift/false) if the specified object or node is not in the tree.

#### Discussion

By referencing the node that contains the object to remove, this method can quickly remove an object from the tree without needing to perform an exhaustive search. To make use of this performance optimization, keep a reference to the node returned when you add elements with the [`add(_:at:)`](gkoctree/add(_:at:).md) or [`add(_:in:)`](gkoctree/add(_:in:).md) methods.

## Parameters

- `node`: The node in the tree containing the object.

## See Also

- [func add(ElementType, at: vector_float3) -> GKOctreeNode](gkoctree/add(_:at:).md)
  Adds an object to the tree corresponding to the specified point in 3D space.
- [func add(ElementType, in: GKBox) -> GKOctreeNode](gkoctree/add(_:in:).md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType) -> Bool](gkoctree/remove(_:).md)
  Searches for the specified object and removes it from the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/remove(_:using:))*