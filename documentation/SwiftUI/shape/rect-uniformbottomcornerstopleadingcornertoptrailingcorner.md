# rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: method

Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.

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
static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self
```

#### Discussion

For the two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each bottom corner to achieve the symmetric look.

## Parameters

- `uniformBottomCorners`: The corner style to apply uniformly to the two bottom corners.
- `topLeadingCorner`: The top leading corner style.
- `topTrailingCorner`: The top trailing corner style.

## See Also

- [init(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style)](concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:).md)
  Creates a rectangle with a corner style set on the bottom two corners uniformly, and two other styles for the top two corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:))*