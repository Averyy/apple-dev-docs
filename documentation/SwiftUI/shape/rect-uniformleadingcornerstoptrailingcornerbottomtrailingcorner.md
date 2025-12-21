# rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: method

A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the leading two corners, while the trailing two corners will each has an indivdual corner style.

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
static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformLeadingCorners`: The corner style to be applied on the leading   two corners uniformly. This shape will first resolve the two corners   individually, then pick the largest resolved radius out of the two and   apply it uniformly to achieve the symmetric look.
- `topTrailingCorner`: The top trailing corner style.
- `bottomTrailingCorner`: The bottom trailing corner style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:))*