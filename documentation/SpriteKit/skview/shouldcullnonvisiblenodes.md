# shouldCullNonVisibleNodes

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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
var shouldCullNonVisibleNodes: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldCullNonVisibleNodes;
```

## Mentions

- [Maximizing Node Drawing Performance](../maximizing-node-drawing-performance.md)

#### Discussion

The default value is [`true`](../../Swift/true.md), meaning that when the scene is rendered, the scene first searches the tree for invisible or offscreen nodes and culls them from the list of nodes to be rendered. Then the remaining (visible) nodes are processed and rendered. This is normally the desired behavior, because Scene Kit avoids expensive processing on nodes that cannot affect the final output. However, if your game is already managing the contents of the scene’s node tree (for example, by removing nodes from the tree when they are offscreen), you can set this to [`false`](../../Swift/false.md) to disable automatic scene culling. Disabling scene culling removes the performance overhead of this check, but each invisible or offscreen node present in the node tree reduces the performance of the renderer.

## See Also

### Configuring Performance Related Toggles
- [var ignoresSiblingOrder: Bool](./ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var allowsTransparency: Bool](./allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.
- [var isAsynchronous: Bool](./isasynchronous.md)
  A Boolean value that indicates whether the content is rendered asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/shouldcullnonvisiblenodes)*