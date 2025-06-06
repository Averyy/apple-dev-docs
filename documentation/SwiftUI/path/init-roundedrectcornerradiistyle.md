# init(roundedRect:cornerRadii:style:)

**Framework**: SwiftUI  
**Kind**: init

Creates a path as the given rounded rectangle, which may have uneven corner radii.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(roundedRect rect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle = .continuous)
```

#### Discussion

This is a convenience function that creates a path of a rounded rectangle. Using this function is more efficient than creating a path and adding a rounded rectangle to it.

## Parameters

- `rect`: A rectangle, specified in user space coordinates.
- `cornerRadii`: The radius of each corner of the rectangle,   specified in user space coordinates.
- `style`: The corner style. Defaults to the   style   if not specified.

## See Also

- [init()](path/init.md)
  Creates an empty path.
- [init(_:)](path/init(_:).md)
  Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn: CGRect)](path/init(ellipsein:).md)
  Creates a path as an ellipse within the given rectangle.
- [init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)](path/init(roundedrect:cornerradius:style:).md)
  Creates a path containing a rounded rectangle.
- [init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)](path/init(roundedrect:cornersize:style:).md)
  Creates a path containing a rounded rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(roundedrect:cornerradii:style:))*