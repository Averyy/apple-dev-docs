# init(roundedRect:cornerWidth:cornerHeight:transform:)

**Framework**: Core Graphics  
**Kind**: init

Create an immutable path of a rounded rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(roundedRect rect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)
```

#### Return Value

A new, immutable path. You are responsible for releasing this object.

#### Discussion

This is a convenience function that creates a path of an rounded rectangle. Using this convenience function is more efficient than creating a mutable path and adding an rectangle to it.

Each corner of the rounded rectangle is one-quarter of an ellipse with axes equal to the `cornerWidth` and `cornerHeight` parameters. The rounded rectangle forms a complete subpath and is oriented in the clockwise direction.

## Parameters

- `rect`: The rectangle to add.
- `cornerWidth`: The width of the rounded corner sections.
- `cornerHeight`: The height of the rounded corner sections.
- `transform`: A pointer to an affine transformation matrix, or   if no transformation is needed. If specified, Core Graphics applies the transformation to the rectangle before it is added to the path.

## See Also

- [init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)](cgpath/init(rect:transform:).md)
  Create an immutable path of a rectangle.
- [init(ellipseIn: CGRect, transform: UnsafePointer<CGAffineTransform>?)](cgpath/init(ellipsein:transform:).md)
  Create an immutable path of an ellipse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/init(roundedrect:cornerwidth:cornerheight:transform:))*