# init(rectOf:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a shape node with a rectangular path centered on the node’s origin.

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
convenience init(rectOf size: CGSize)
```

```objc
+ (instancetype) shapeNodeWithRectOfSize:(CGSize) size;
```

## Return Value

A new shape node.

## Parameters

- `size`: The size of the rectangle.

## See Also

### Creating a Shape from a Rectangle
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates a shape node with a rectangular path.
- [convenience init(rect: CGRect, cornerRadius: CGFloat)](./init%28rect,cornerradius%29.md)
  Creates a shape with a rectangular path that has rounded corners.
- [convenience init(rectOf: CGSize, cornerRadius: CGFloat)](./init%28rectof,cornerradius%29.md)
  Creates a shape with a rectangular path that has rounded corners centered on the node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(rectof:))*