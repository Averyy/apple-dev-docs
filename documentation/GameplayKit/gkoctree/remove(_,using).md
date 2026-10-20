# remove(_:using:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) removeElement:(ElementType) element withNode:(GKOctreeNode *) node;
```

#### Return Value

[`true`](../../Swift/true.md) if the object was removed from the tree. [`false`](../../Swift/false.md) if the specified object or node is not in the tree.

#### Discussion

By referencing the node that contains the object to remove, this method can quickly remove an object from the tree without needing to perform an exhaustive search. To make use of this performance optimization, keep a reference to the node returned when you add elements with the [`add(_:at:)`](./add%28_,at%29.md) or [`add(_:in:)`](./add%28_,in%29.md) methods.

## Parameters

- `node`: The node in the tree containing the object.

## See Also

### Adding and Removing Elements
- [func add(ElementType, at: vector_float3) -> GKOctreeNode](./add%28_,at%29.md)
  Adds an object to the tree corresponding to the specified point in 3D space.
- [func add(ElementType, in: GKBox) -> GKOctreeNode](./add%28_,in%29.md)
  Adds an object to the tree corresponding to the specified volume of 3D space.
- [func remove(ElementType) -> Bool](./remove%28_%29.md)
  Searches for the specified object and removes it from the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/remove(_:using:))*