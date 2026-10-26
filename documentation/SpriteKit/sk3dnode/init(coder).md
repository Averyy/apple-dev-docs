# init(coder:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Tells you when to initialize a 3D node that has been unarchived.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

#### Discussion

Do not call this function directly; it is called by the system when you should initialize a 3D node that has been unarchived.

## See Also

### Creating 3D Nodes
- [init(viewportSize: CGSize)](./init%28viewportsize%29.md)
  Initializes a new 3D node.
- [+ nodeWithViewportSize:](./nodewithviewportsize_.md)
  Creates and initializes a new 3D node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/init(coder:))*