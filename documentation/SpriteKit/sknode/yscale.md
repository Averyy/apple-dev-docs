# yScale

**Framework**: SpriteKit  
**Kind**: property

A scaling factor that multiplies the height of a node and its children.

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
var yScale: CGFloat { get set }
```

## Mentions

- [Getting Started with a Camera](getting-started-with-a-camera.md)
- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)
- [About Node Property Propagation](about-node-property-propagation.md)
- [Getting Started with Nodes](getting-started-with-nodes.md)

#### Discussion

The [`yScale`](sknode/yscale.md) property scales the height of the node and all of its descendants. The scale value affects how a node’s frame is calculated, its hit test area, how it is drawn, and other similar characteristics. The default value is `1.0`.

## See Also

- [var zRotation: CGFloat](sknode/zrotation.md)
  The Euler rotation about the z axis (in radians).
- [func setScale(CGFloat)](sknode/setscale(_:).md)
  Sets the [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) properties of the node.
- [var xScale: CGFloat](sknode/xscale.md)
  A scaling factor that multiplies the width of a node and its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/yscale)*