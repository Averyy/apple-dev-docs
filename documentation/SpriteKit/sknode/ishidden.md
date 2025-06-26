# isHidden

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether a node and its descendants are rendered.

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
var isHidden: Bool { get set }
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)
- [About Node Property Propagation](about-node-property-propagation.md)

#### Discussion

When hidden, a node and its descendants are not rendered. However, they still exist in the scene and continue to interact in other ways. For example, the node’s actions still run and the node can still be intersected with other nodes. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var alpha: CGFloat](sknode/alpha.md)
  The transparency value applied to the node’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/ishidden)*