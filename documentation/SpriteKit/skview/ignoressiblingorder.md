# ignoresSiblingOrder

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var ignoresSiblingOrder: Bool { get set }
```

## Mentions

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
- [About Node Drawing Order](about-node-drawing-order.md)

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false), which means that when multiple nodes share the same z position, those nodes are sorted and rendered in a deterministic order. Parents are rendered before their children, and siblings are rendered in array order. When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the position of the nodes in the tree is ignored when determining the rendering order. The rendering order of nodes at the same z position is arbitrary and may change every time a new frame is rendered. When sibling and parent order is ignored, SpriteKit applies additional optimizations to improve rendering performance. If you need nodes to be rendered in a specific and deterministic order, you must set the z position of those nodes.

## See Also

- [var shouldCullNonVisibleNodes: Bool](skview/shouldcullnonvisiblenodes.md)
  A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.
- [var allowsTransparency: Bool](skview/allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.
- [var isAsynchronous: Bool](skview/isasynchronous.md)
  A Boolean value that indicates whether the content is rendered asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/ignoressiblingorder)*