# nodeWithViewportSize:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates and initializes a new 3D node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) nodeWithViewportSize:(CGSize) viewportSize;
```

## Return Value

A newly created and initialized [`SK3DNode`](../sk3dnode.md) object.

## Discussion

The node must be configured with a SceneKit scene before it renders anything.

## Parameters

- `viewportSize`: The size of the node’s rendered image.

## See Also

### Creating 3D Nodes
- [init(viewportSize: CGSize)](./init%28viewportsize%29.md)
  Initializes a new 3D node.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize a 3D node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/nodewithviewportsize:)*