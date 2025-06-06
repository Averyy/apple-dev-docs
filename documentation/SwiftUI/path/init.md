# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates an empty path, then executes a closure to add its initial elements.

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
init(_ callback: (inout Path) -> ())
```

## Parameters

- `callback`: The Swift function that will be called to   initialize the new path.

## See Also

- [init()](path/init.md)
  Creates an empty path.
- [init(ellipseIn: CGRect)](path/init(ellipsein:).md)
  Creates a path as an ellipse within the given rectangle.
- [init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)](path/init(roundedrect:cornerradius:style:).md)
  Creates a path containing a rounded rectangle.
- [init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)](path/init(roundedrect:cornersize:style:).md)
  Creates a path containing a rounded rectangle.
- [init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)](path/init(roundedrect:cornerradii:style:).md)
  Creates a path as the given rounded rectangle, which may have uneven corner radii.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(_:))*