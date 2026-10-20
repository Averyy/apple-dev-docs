# alpha

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The transparency value applied to the node’s contents.

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
var alpha: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat alpha;
```

## Mentions

- [About Node Property Propagation](../about-node-property-propagation.md)
- [Controlling User Interaction on Nodes](../controlling-user-interaction-on-nodes.md)
- [Getting Started with Nodes](../getting-started-with-nodes.md)

#### Discussion

The default value is `1.0`.

The [`SKNode`](../sknode.md) class does not perform drawing, but many of its subclasses do. When a node or any of its descendants are drawn, the alpha component of each pixel is multiplied by the node’s [`alpha`](./alpha.md) property and then clamped to the range `0.0`-`1.0`. This modified alpha value is used to blend the pixel into the framebuffer. Subclasses that render content define properties that determine the blending operations used in conjunction with the alpha value to blend pixels into the parent’s framebuffer.

## See Also

### Altering Node Visibility
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether a node and its descendants are rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/alpha)*