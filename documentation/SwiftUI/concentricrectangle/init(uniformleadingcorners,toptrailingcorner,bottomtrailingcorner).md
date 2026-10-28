# init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.

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
init(uniformLeadingCorners: Edge.Corner.Style = .concentric, topTrailingCorner: Edge.Corner.Style = .concentric, bottomTrailingCorner: Edge.Corner.Style = .concentric)
```

## Discussion

For the two leading corners, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each leading corner to achieve the symmetric look.

## Parameters

- `uniformLeadingCorners`: The corner style to apply to the leading two corners uniformly.
- `topTrailingCorner`: The corner style for the top trailing corner.
- `bottomTrailingCorner`: The corner style for the bottom trailing corner.

## See Also

### Creating a rectangle with uniform leading corners
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](../shape/rect%28uniformleadingcorners,toptrailingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:))*