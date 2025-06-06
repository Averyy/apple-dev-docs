# init(boundingQuad:minimumCellSize:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a quadtree with the specified dimensions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(boundingQuad quad: GKQuad, minimumCellSize minCellSize: Float)
```

#### Return Value

A new quadtree object.

#### Discussion

The `minCellSize` parameter controls the memory usage and performance of the tree. A lower value causes the tree to make more spatial divisions when adding elements; a higher value causes the tree to create fewer such divisions, but store more elements in each node. Which direction leads to better performance depends on the number and spatial arrangement of the elements you add to the tree—for best results, profile with different values to find one best suited to your app or game.

## Parameters

- `quad`: The axis-aligned bounding rectangle encompassing all possible elements of the tree. Elements added to the tree must lie entirely within this rectangle.
- `minCellSize`: The minimum dimension (width and height) of a node in the tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtree/init(boundingquad:minimumcellsize:))*