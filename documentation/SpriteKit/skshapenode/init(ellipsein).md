# init(ellipseIn:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a shape node with an elliptical path that fills the specified rectangle.

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
convenience init(ellipseIn rect: CGRect)
```

```objc
+ (instancetype) shapeNodeWithEllipseInRect:(CGRect) rect;
```

## Return Value

A new shape node.

## Parameters

- `rect`: A rectangle, relative to the node’s origin.

## See Also

### Creating an Ellipse Shape
- [convenience init(ellipseOf: CGSize)](./init%28ellipseof%29.md)
  Creates a shape node with an elliptical path centered on the node’s origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(ellipsein:))*