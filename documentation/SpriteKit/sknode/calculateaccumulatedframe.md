# calculateAccumulatedFrame()

**Framework**: SpriteKit  
**Kind**: method

Returns a rectangle in the parent’s coordinate system that contains the position and size of itself and all child nodes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
func calculateAccumulatedFrame() -> CGRect
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)
- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)

#### Discussion

The frame takes into the account the cumulative effect of the [`xScale`](sknode/xscale.md), [`yScale`](sknode/yscale.md), and [`zRotation`](sknode/zrotation.md) properties of each node in the subtree.

Listing 1 shows, in Swift, how [`calculateAccumulatedFrame()`](sknode/calculateaccumulatedframe().md) can be used display the bounding box of a shape node. The child node, although smaller than its parent, is rotated by 30° so that its bounds extend beyond its parent’s bounds. After `childNode` has been added to `parentNode`, a further shape node, `boundingBoxNode`, is created with its size based on the accumulated frame of parentNode.

Listing 1. Displaying the accumulated frame of a shape node

```swift
let parentNode = SKShapeNode(rectOf: CGSize(width: 500, height: 500))
parentNode.lineWidth = 2
parentNode.strokeColor = .blue
parentNode.fillColor = .clear
     
let childNode = SKShapeNode(rectOf: CGSize(width: 400, height: 400))
childNode.strokeColor = .red
childNode.fillColor = .clear
childNode.zRotation = -CGFloat.pi / 6 // pi / 6 = 30°
     
parentNode.addChild(childNode)
     
let boundingBoxNode = SKShapeNode(rectOf: parentNode.calculateAccumulatedFrame().size)
boundingBoxNode.lineWidth = 1
boundingBoxNode.strokeColor = .black
boundingBoxNode.fillColor = .clear
boundingBoxNode.path = boundingBoxNode.path?.copy(dashingWithPhase: 0,
                                                  lengths: [10,10])
     
parentNode.addChild(boundingBoxNode)
```

The figure below shows the result of Listing 1 with `parentNode` rendered in blue, `childNode` rendered in red and the `boundingBoxNode` rendered with a dashed line.

![Displaying the accumulated frame of a shape node](https://docs-assets.developer.apple.com/published/027aac3e4a73961ddb2b9a41f5418b27/media-2793217%402x.png)

## See Also

- [var frame: CGRect](sknode/frame.md)
  A rectangle in the parent’s coordinate system that contains the node’s content, ignoring the node’s children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/calculateaccumulatedframe())*