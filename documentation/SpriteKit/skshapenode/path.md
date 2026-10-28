# path

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The path that defines the shape.

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
var path: CGPath? { get set }
```

```objc
@property (nonatomic, nullable) CGPathRef path;
```

## Mentions

- [Getting Started with Shape Nodes](../getting-started-with-shape-nodes.md)

## Discussion

The path is defined in the node’s coordinate space.

## See Also

### Creating a Shape from a Path
- [convenience init(path: CGPath)](./init%28path%29.md)
  Creates a shape node from a Core Graphics path.
- [convenience init(path: CGPath, centered: Bool)](./init%28path,centered%29.md)
  Creates a shape node from a Core Graphics path, centered around its position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/path)*