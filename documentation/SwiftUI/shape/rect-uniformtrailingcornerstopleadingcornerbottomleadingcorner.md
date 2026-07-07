# rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)

**Framework**: SwiftUI  
**Kind**: method

Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.

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
static func rect(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style) -> Self
```

#### Discussion

For the two trailing corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each trailing corner to achieve the symmetric look.

## Parameters

- `uniformTrailingCorners`: The corner style to apply uniformly to the two trailing corners.
- `topLeadingCorner`: The top leading corner style.
- `bottomLeadingCorner`: The bottom leading corner style.

## See Also

- [init(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style)](concentricrectangle/init(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:).md)
  Creates a rectangle with a corner style set on the trailing two corners uniformly, and two other styles for the leading two corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:))*