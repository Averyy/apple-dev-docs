# init(rect:transform:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Create an immutable path of a rectangle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)
```

```c
extern CGPathRefCGPathCreateWithRect(CGRect rect, const CGAffineTransform *transform);
```

## Return Value

A new, immutable path. You are responsible for releasing this object.

## Discussion

This is a convenience function that creates a path of an rectangle. Using this convenience function is more efficient than creating a mutable path and adding an rectangle to it.

Calling this function is equivalent to using [`CGRectGetMinX(_:)`](../cgrectgetminx%28_%29.md) and related functions to find the corners of the rectangle, then using the [`CGPathMoveToPoint`](../cgpathmovetopoint.md), [`CGPathAddLineToPoint`](../cgpathaddlinetopoint.md), and [`closeSubpath()`](../cgmutablepath/closesubpath%28%29.md) functions to draw the rectangle.

## Parameters

- `rect`: The rectangle to add.
- `transform`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the rectangle before it is added to the path.

## See Also

### Creating Graphics Paths
- [init(ellipseIn: CGRect, transform: UnsafePointer<CGAffineTransform>?)](./init%28ellipsein,transform%29.md)
  Create an immutable path of an ellipse.
- [init(roundedRect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)](./init%28roundedrect,cornerwidth,cornerheight,transform%29.md)
  Create an immutable path of a rounded rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/init(rect:transform:))*