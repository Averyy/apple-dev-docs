# rect(cornerRadii:style:)

**Framework**: SwiftUI  
**Kind**: method

A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.

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
@export(implementation)
static func rect(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle = .continuous) -> Self
```

## See Also

- [static var rect: Rectangle](shape/rect.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(cornerradius:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(corners: Edge.Corner.Style, isUniform: Bool) -> Self](shape/rect(corners:isuniform:).md)
  Creates a rectangle with the same corner style set on four corners.
- [static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self](shape/rect(cornersize:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:).md)
  Creates a rectangle with individual styles for each corner.
- [static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat, bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:).md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:).md)
  Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:).md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, uniformTrailingCorners: Edge.Corner.Style) -> Self](shape/rect(uniformleadingcorners:uniformtrailingcorners:).md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
- [static func rect(uniformTopCorners: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:).md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
- [static func rect(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style) -> Self](shape/rect(uniformtopcorners:uniformbottomcorners:).md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
- [static func rect(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:).md)
  Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(cornerradii:style:))*