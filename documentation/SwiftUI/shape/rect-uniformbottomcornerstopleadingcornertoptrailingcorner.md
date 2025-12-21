# rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)

**Framework**: SwiftUI  
**Kind**: method

A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the bottom two corners, while the top two corners will each has an indivdual corner style.

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
static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformBottomCorners`: The corner style to be applied on the bottom   two corners uniformly. This shape will first resolve the two corners   individually, then pick the largest resolved radius out of the two and   apply it uniformly to achieve the symmetric look.
- `topLeadingCorner`: The top leading corner style.
- `topTrailingCorner`: The top trailing corner style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:))*