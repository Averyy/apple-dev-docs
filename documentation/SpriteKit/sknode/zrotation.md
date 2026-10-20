# zRotation

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The Euler rotation about the z axis (in radians).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var zRotation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat zRotation;
```

## Mentions

- [About Node Property Propagation](../about-node-property-propagation.md)
- [About SpriteKit Coordinate Systems](../about-spritekit-coordinate-systems.md)
- [Getting Started with a Camera](../getting-started-with-a-camera.md)
- [Getting Started with Nodes](../getting-started-with-nodes.md)
- [Making Physics Bodies Move](../making-physics-bodies-move.md)

#### Discussion

The default value is `0.0`, which indicates no rotation. A positive value indicates a counterclockwise rotation. When the coordinate system is rotated, it affects the node and its descendants. The rotation affects the node’s [`frame`](./frame.md) property, hit testing, rendering, and other similar characteristics.

## See Also

### Scaling and Rotating
- [func setScale(CGFloat)](./setscale%28_%29.md)
  Sets the [`xScale`](./xscale.md) and [`yScale`](./yscale.md) properties of the node.
- [var xScale: CGFloat](./xscale.md)
  A scaling factor that multiplies the width of a node and its children.
- [var yScale: CGFloat](./yscale.md)
  A scaling factor that multiplies the height of a node and its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/zrotation)*