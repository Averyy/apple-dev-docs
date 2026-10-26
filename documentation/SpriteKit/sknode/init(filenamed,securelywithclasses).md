# init(fileNamed:securelyWithClasses:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
convenience init(fileNamed filename: String, securelyWithClasses classes: Set<AnyHashable>) throws
```

```objc
+ (instancetype) nodeWithFileNamed:(NSString *) filename securelyWithClasses:(NSSet<Class> *) classes andError:(NSError **) error;
```

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
- [+ node](./node.md)
  Creates a new node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/init(filenamed:securelywithclasses:))*