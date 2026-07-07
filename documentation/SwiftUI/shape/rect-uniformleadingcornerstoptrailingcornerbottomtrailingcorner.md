# rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: method

Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@export(implementation)
static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self
```

#### Discussion

For the two leading corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each leading corner to achieve the symmetric look.

## Parameters

- `uniformLeadingCorners`: The corner style to apply uniformly to the two leading corners.
- `topTrailingCorner`: The top trailing corner style.
- `bottomTrailingCorner`: The bottom trailing corner style.

## See Also

- [init(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style)](concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:).md)
  Creates a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:))*