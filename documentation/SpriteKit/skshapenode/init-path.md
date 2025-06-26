# init(path:)

**Framework**: SpriteKit  
**Kind**: init

Creates a shape node from a Core Graphics path.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(path: CGPath)
```

#### Return Value

A new shape node.

## Parameters

- `path`: The Core Graphics path to use. The path is relative to the node’s origin.

## See Also

- [convenience init(path: CGPath, centered: Bool)](skshapenode/init(path:centered:).md)
  Creates a shape node from a Core Graphics path, centered around its position.
- [var path: CGPath?](skshapenode/path.md)
  The path that defines the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(path:))*