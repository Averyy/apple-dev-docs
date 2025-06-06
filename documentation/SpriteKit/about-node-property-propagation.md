# About Node Property Propagation

**Framework**: SpriteKit

Learn which properties of a node affect its child nodes.

#### Overview

Changing certain properties on a node can propogate to its decendents:

| Property | Description |
| --- | --- |
| [`xScale`](sknode/xscale.md), [`yScale`](sknode/yscale.md) | The node’s coordinate system is scaled by these two factors. This property affects coordinate conversion, the node’s frame, drawing, and hit testing. Its descendants are similarly scaled. |
| [`zPosition`](sknode/zposition.md) | The node’s draw order. Nodes with a higher `zPosition` are rendered above nodes with a lower `zPosition`. This value propagates to its descendants such that a node’s `zPosition` is equal to that of its parent node, plus any value it holds in its own `zPosition` property. |
| [`zRotation`](sknode/zrotation.md) | The node’s coordinate system is rotated. This property affects coordinate conversion, the node’s frame, drawing, and hit testing. Its descendants are similarly scaled. |
| [`alpha`](sknode/alpha.md) | If the node is rendered using a blend mode, the alpha value is multiplied into any alpha value before the blend operation takes place. The descendants are similarly affected. |
| [`isHidden`](sknode/ishidden.md) | If a node is hidden, the node and its descendants are not rendered. |
| [`speed`](sknode/speed.md) | The speed at which a node processes actions is multiplied by this value. The descendants are similarly affected. |

The net effect is that a child node is rendered based not only on its own properties but also on the properties of its ancestors.

__


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/about-node-property-propagation)*