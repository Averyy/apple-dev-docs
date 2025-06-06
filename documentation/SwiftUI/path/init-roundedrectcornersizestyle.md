# init(roundedRect:cornerSize:style:)

**Framework**: SwiftUI  
**Kind**: init

Creates a path containing a rounded rectangle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(roundedRect rect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle = .continuous)
```

#### Discussion

This is a convenience function that creates a path of a rounded rectangle. Using this convenience function is more efficient than creating a path and adding a rounded rectangle to it.

## Parameters

- `rect`: A rectangle, specified in user space coordinates.
- `cornerSize`: The size of the corners, specified in user space   coordinates.
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
- [init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)](path/init(roundedrect:cornerradii:style:).md)
  Creates a path as the given rounded rectangle, which may have uneven corner radii.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(roundedrect:cornersize:style:))*