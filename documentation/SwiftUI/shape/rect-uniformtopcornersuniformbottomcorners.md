# rect(uniformTopCorners:uniformBottomCorners:)

**Framework**: SwiftUI  
**Kind**: method

Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.

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
static func rect(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style) -> Self
```

#### Discussion

For the two top corners and two bottom corners, the system calculates the radius for each corner first. Then, it selects the largest top radius and applies it to each top corner, and it selects the largest bottom radius and applies it to each bottom corner to achieve the symmetric look.

## Parameters

- `uniformTopCorners`: The corner style to apply uniformly to the two top corners.
- `uniformBottomCorners`: The corner style to apply uniformly to the two bottom corners.

## See Also

- [init(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style)](concentricrectangle/init(uniformtopcorners:uniformbottomcorners:).md)
  Creates a rectangle with a corner style set on the top two corners uniformly, and another style set on the bottom two corners uniformly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:))*