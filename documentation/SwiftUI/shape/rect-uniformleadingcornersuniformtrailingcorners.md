# rect(uniformLeadingCorners:uniformTrailingCorners:)

**Framework**: SwiftUI  
**Kind**: method

A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the leading two corners, while another corner style will be uniformly applied to the trailing two.

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
static func rect(uniformLeadingCorners: Edge.Corner.Style, uniformTrailingCorners: Edge.Corner.Style) -> Self
```

## Parameters

- `uniformLeadingCorners`: The corner style to be applied on the leading   two corners uniformly. This shape will first resolve the two corners   individually, then pick the largest resolved radius out of the two and   apply it uniformly to achieve the symmetric look.
- `uniformTrailingCorners`: The corner style to be applied on the   trailing two corners uniformly. This shape will first resolve the two   corners individually, then pick the largest resolved radius out of the   two and apply it uniformly to achieve the symmetric look.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:))*