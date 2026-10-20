# add(_:in:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Adds an object to the tree corresponding to the specified region of 2D space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ element: ElementType, in quad: GKQuad) -> GKQuadtreeNode
```

```objc
- (GKQuadtreeNode *) addElement:(ElementType) element withQuad:(GKQuad) quad;
```

#### Return Value

The tree node containing the newly added object.

#### Discussion

The [`GKQuadtree`](../gkquadtree.md) class automatically creates nodes to manage the objects you add to the tree. If you expect to remove an element you’ve added, keep a reference to the node this method returns so you can use the [`remove(_:using:)`](./remove%28_,using%29.md) method to remove that object quickly.

## Parameters

- `element`: The object to add to the tree.
- `quad`: The axis-aligned bounding region in 2D space to which the object corresponds.

## See Also

### Adding and Removing Elements
- [func add(ElementType, at: vector_float2) -> GKQuadtreeNode](./add%28_,at%29.md)
  Adds an object to the tree corresponding to the specified point in 2D space.
- [func remove(ElementType, using: GKQuadtreeNode) -> Bool](./remove%28_,using%29.md)
  Removes the specified object from the tree, using a reference to its containing node.
- [func remove(ElementType) -> Bool](./remove%28_%29.md)
  Searches for the specified object and removes it from the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtree/add(_:in:))*