# init(rectOf:cornerRadius:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a shape with a rectangular path that has rounded corners centered on the node’s position.

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
convenience init(rectOf size: CGSize, cornerRadius: CGFloat)
```

```objc
+ (instancetype) shapeNodeWithRectOfSize:(CGSize) size cornerRadius:(CGFloat) cornerRadius;
```

## Return Value

A new shape node.

## Parameters

- `size`: The size of the rectangle.
- `cornerRadius`: The radius of the rounded corners. The radius should not be a negative number. The value should be no larger than half of the rectangle’s width or height, whichever is smaller.

## See Also

### Creating a Shape from a Rectangle
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates a shape node with a rectangular path.
- [convenience init(rectOf: CGSize)](./init%28rectof%29.md)
  Creates a shape node with a rectangular path centered on the node’s origin.
- [convenience init(rect: CGRect, cornerRadius: CGFloat)](./init%28rect,cornerradius%29.md)
  Creates a shape with a rectangular path that has rounded corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(rectof:cornerradius:))*