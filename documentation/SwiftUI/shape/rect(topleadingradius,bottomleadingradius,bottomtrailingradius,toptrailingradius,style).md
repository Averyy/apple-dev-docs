# rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func rect(topLeadingRadius: CGFloat = 0, bottomLeadingRadius: CGFloat = 0, bottomTrailingRadius: CGFloat = 0, topTrailingRadius: CGFloat = 0, style: RoundedCornerStyle = .continuous) -> Self
```

Available when `Self` is `UnevenRoundedRectangle`.

## See Also

### Getting rectangles
- [static var rect: Rectangle](./rect.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [static func rect(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle) -> Self](./rect%28cornerradii,style%29.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self](./rect%28cornerradius,style%29.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(corners: Edge.Corner.Style, isUniform: Bool) -> Self](./rect%28corners,isuniform%29.md)
  Creates a rectangle with the same corner style set on four corners.
- [static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self](./rect%28cornersize,style%29.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./rect%28topleadingcorner,toptrailingcorner,bottomleadingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with individual styles for each corner.
- [static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self](./rect%28uniformbottomcorners,topleadingcorner,toptrailingcorner%29.md)
  Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./rect%28uniformleadingcorners,toptrailingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, uniformTrailingCorners: Edge.Corner.Style) -> Self](./rect%28uniformleadingcorners,uniformtrailingcorners%29.md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
- [static func rect(uniformTopCorners: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./rect%28uniformtopcorners,bottomleadingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
- [static func rect(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style) -> Self](./rect%28uniformtopcorners,uniformbottomcorners%29.md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
- [static func rect(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style) -> Self](./rect%28uniformtrailingcorners,topleadingcorner,bottomleadingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:))*