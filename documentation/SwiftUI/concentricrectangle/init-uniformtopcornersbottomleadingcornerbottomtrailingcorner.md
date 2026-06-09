# init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: init

Creates a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.

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
init(uniformTopCorners: Edge.Corner.Style = .concentric, bottomLeadingCorner: Edge.Corner.Style = .concentric, bottomTrailingCorner: Edge.Corner.Style = .concentric)
```

#### Discussion

For the two top corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each top corner to achieve the symmetric look.

## Parameters

- `uniformTopCorners`: The corner style to apply to the top two corners uniformly.
- `bottomLeadingCorner`: The corner style for the bottom leading corner.
- `bottomTrailingCorner`: The corner style for the bottom trailing corner.

## See Also

- [static func rect(uniformTopCorners: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:).md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:))*