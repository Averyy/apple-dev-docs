# frame

**Framework**: SpriteKit  
**Kind**: property

A rectangle in the parent’s coordinate system that contains the node’s content, ignoring the node’s children.

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
var frame: CGRect { get }
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)
- [Getting Started with Sprite Nodes](getting-started-with-sprite-nodes.md)
- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)

#### Discussion

The frame is the smallest rectangle that contains the node’s content, taking into account the node’s [`xScale`](sknode/xscale.md), [`yScale`](sknode/yscale.md), and [`zRotation`](sknode/zrotation.md) properties.

Since `SKNode` does not draw content of its own, its frame size is arbitrary; it’s the visual subclasses of `SKNode` that do draw that define the frame’s size with a meaningful value that encloses its visual content.

To get a rect that encloses all the child nodes of an `SKNode` parent object, use [`calculateAccumulatedFrame()`](sknode/calculateaccumulatedframe().md).

## See Also

- [func calculateAccumulatedFrame() -> CGRect](sknode/calculateaccumulatedframe.md)
  Returns a rectangle in the parent’s coordinate system that contains the position and size of itself and all child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/frame)*