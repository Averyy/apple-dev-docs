# path

**Framework**: SpriteKit  
**Kind**: property

The path that defines the shape.

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
var path: CGPath? { get set }
```

## Mentions

- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)

#### Discussion

The path is defined in the node’s coordinate space.

## See Also

- [convenience init(path: CGPath)](skshapenode/init(path:).md)
  Creates a shape node from a Core Graphics path.
- [convenience init(path: CGPath, centered: Bool)](skshapenode/init(path:centered:).md)
  Creates a shape node from a Core Graphics path, centered around its position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/path)*