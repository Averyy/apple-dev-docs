# isHidden

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether a node and its descendants are rendered.

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
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Mentions

- [About Node Property Propagation](../about-node-property-propagation.md)
- [Getting Started with Nodes](../getting-started-with-nodes.md)

#### Discussion

When hidden, a node and its descendants are not rendered. However, they still exist in the scene and continue to interact in other ways. For example, the node’s actions still run and the node can still be intersected with other nodes. The default value is [`false`](../../Swift/false.md).

## See Also

### Altering Node Visibility
- [var alpha: CGFloat](./alpha.md)
  The transparency value applied to the node’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/ishidden)*