# shouldCullNonVisibleNodes

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldCullNonVisibleNodes: Bool { get set }
```

## Mentions

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true), meaning that when the scene is rendered, the scene first searches the tree for invisible or offscreen nodes and culls them from the list of nodes to be rendered. Then the remaining (visible) nodes are processed and rendered. This is normally the desired behavior, because Scene Kit avoids expensive processing on nodes that cannot affect the final output. However, if your game is already managing the contents of the scene’s node tree (for example, by removing nodes from the tree when they are offscreen), you can set this to [`false`](https://developer.apple.com/documentation/Swift/false) to disable automatic scene culling. Disabling scene culling removes the performance overhead of this check, but each invisible or offscreen node present in the node tree reduces the performance of the renderer.

## See Also

- [var ignoresSiblingOrder: Bool](skview/ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var allowsTransparency: Bool](skview/allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.
- [var isAsynchronous: Bool](skview/isasynchronous.md)
  A Boolean value that indicates whether the content is rendered asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/shouldcullnonvisiblenodes)*