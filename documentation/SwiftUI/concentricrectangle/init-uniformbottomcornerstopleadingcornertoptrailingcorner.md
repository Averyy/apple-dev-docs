# init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: init

Creates a rectangle with a corner style set on the bottom two corners uniformly, and two other styles for the top two corners respectively.

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
init(uniformBottomCorners: Edge.Corner.Style = .concentric, topLeadingCorner: Edge.Corner.Style = .concentric, topTrailingCorner: Edge.Corner.Style = .concentric)
```

#### Discussion

For the two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each bottom corner to achieve the symmetric look.

## Parameters

- `uniformBottomCorners`: The corner style to apply to the bottom two corners uniformly.
- `topLeadingCorner`: The corner style for the top leading corner.
- `topTrailingCorner`: The corner style for the top trailing corner.

## See Also

- [static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:).md)
  Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:))*