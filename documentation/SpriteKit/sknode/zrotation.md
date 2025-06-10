# zRotation

**Framework**: SpriteKit  
**Kind**: property

The Euler rotation about the z axis (in radians).

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
var zRotation: CGFloat { get set }
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)
- [About SpriteKit Coordinate Systems](about-spritekit-coordinate-systems.md)
- [Getting Started with a Camera](getting-started-with-a-camera.md)
- [About Node Property Propagation](about-node-property-propagation.md)
- [Making Physics Bodies Move](making-physics-bodies-move.md)

#### Discussion

The default value is `0.0`, which indicates no rotation. A positive value indicates a counterclockwise rotation. When the coordinate system is rotated, it affects the node and its descendants. The rotation affects the node’s [`frame`](sknode/frame.md) property, hit testing, rendering, and other similar characteristics.

## See Also

- [func setScale(CGFloat)](sknode/setscale(_:).md)
  Sets the [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) properties of the node.
- [var xScale: CGFloat](sknode/xscale.md)
  A scaling factor that multiplies the width of a node and its children.
- [var yScale: CGFloat](sknode/yscale.md)
  A scaling factor that multiplies the height of a node and its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/zrotation)*