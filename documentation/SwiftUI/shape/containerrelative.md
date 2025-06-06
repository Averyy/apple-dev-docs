# containerRelative

**Framework**: SwiftUI  
**Kind**: property

A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var containerRelative: ContainerRelativeShape { get }
```

## See Also

- [static var buttonBorder: ButtonBorderShape](shape/buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
- [static var capsule: Capsule](shape/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](shape/capsule(style:).md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](shape/circle.md)
  A circle centered on the frame of the view containing it.
- [static var ellipse: Ellipse](shape/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var rect: Rectangle](shape/rect.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [static func rect(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle) -> Self](shape/rect(cornerradii:style:).md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(cornerradius:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self](shape/rect(cornersize:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat, bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:).md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/containerrelative)*