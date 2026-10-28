# node

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a new node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
+ (instancetype) node;
```

## Return Value

A newly initialized node.

## Discussion

The [`SKNode`](../sknode.md) class does not draw or perform any tasks directly, so it is more common to instantiate a node subclass instead. However, you might create an `SKNode` object to organize other related nodes in the node tree.

## See Also

### First Steps
- [Getting Started with Nodes](../getting-started-with-nodes.md)
  Learn about the fundamental properties that provide a foundation for all other nodes.
- [init()](./init%28%29.md)
  Initializes a blank node.
- [convenience init?(fileNamed: String)](./init%28filenamed%29.md)
  Creates a new node by loading an archive file from the game’s main bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Called when a node is initialized from an .sks file.
- [convenience init(fileNamed: String, securelyWithClasses: Set<AnyHashable>) throws](./init%28filenamed,securelywithclasses%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/node)*