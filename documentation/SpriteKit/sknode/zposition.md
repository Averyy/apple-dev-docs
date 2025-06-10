# zPosition

**Framework**: SpriteKit  
**Kind**: property

The height of the node relative to its parent.

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
var zPosition: CGFloat { get set }
```

## Mentions

- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
- [About Node Drawing Order](about-node-drawing-order.md)
- [About Node Property Propagation](about-node-property-propagation.md)
- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
- [Getting Started with Nodes](getting-started-with-nodes.md)

#### Discussion

The default value is `0.0`. The positive z axis is projected toward the viewer so that nodes with larger z-position values are closer to the viewer. When a node tree is rendered, the height of each node (in absolute coordinates) is calculated and then all nodes in the tree are rendered from smallest z-position value to largest z-position value. If multiple nodes share the same z-position, those nodes are sorted so that parent nodes are drawn before their children, and siblings are rendered in the order that they appear in their parent’s [`children`](sknode/children.md) array. Hit-testing is processed in the opposite order.

The [`SKView`](skview.md) class’s [`ignoresSiblingOrder`](skview/ignoressiblingorder.md) property controls whether node sorting is enabled for nodes at the same z-position.

> ❗ **Important**:  Descendants of an effect node or a crop node are not rendered with other nodes in the same tree. An effect node ([`SKEffectNode`](skeffectnode.md)) renders its children into a private framebuffer as a separate node tree, then the composited image is rendered into the tree that contains the effect node. A crop node ([`SKCropNode`](skcropnode.md)) works similarly; it renders the mask separately, then uses the mask to render its actual descendants into the tree that contains the crop node.

##### Using a Nodes Depth to Add Effects

SpriteKit uses the [`zPosition`](sknode/zposition.md) value only to determine the hit testing and drawing order. You can also the z position to implement your own game effects. For example, you might use the height of a node to determine how it is rendered or how it moves onscreen. In this way, you can simulate fog or parallax effects. SpriteKit does not create these effects for you. Usually, you implement them by processing the scene immediately before it is rendered.

## See Also

- [About Node Drawing Order](about-node-drawing-order.md)
  Understand how SpriteKit layers your scene’s nodes from top to bottom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/zposition)*