# remove(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) removeElement:(ElementType) element;
```

#### Return Value

[`true`](../../Swift/true.md) if the object was removed from the tree. [`false`](../../Swift/false.md) if the specified object is not in the tree.

#### Discussion

The tree does not directly reference its elements—octrees are optimized to search for elements based on spatial positions—so this method must exhaustively search the entire tree to find the object to remove. For quicker removal, keep a reference to the [`GKOctreeNode`](../gkoctreenode.md) object returned when you add an object to the tree, and call the [`remove(_:using:)`](./remove%28_,using%29.md) method instead.

## Parameters

- `element`: The object to be removed from the tree.

## See Also

### Adding and Removing Elements
- [func add(ElementType, at: vector_float3) -> GKOctreeNode](./add%28_,at%29.md)
  Adds an object to the tree corresponding to the specified point in 3D space.
- [func add(ElementType, in: GKBox) -> GKOctreeNode](./add%28_,in%29.md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType, using: GKOctreeNode) -> Bool](./remove%28_,using%29.md)
  Removes the specified object from the tree, using a reference to its containing node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/remove(_:))*