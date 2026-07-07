# rect(corners:isUniform:)

**Framework**: SwiftUI  
**Kind**: method

Creates a rectangle with the same corner style set on four corners.

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
static func rect(corners: Edge.Corner.Style, isUniform: Bool = false) -> Self
```

#### Discussion

When you provide `false` for `isUniform`, the system may calculate a different radius for each corner. This can happen when the rectangle is not centered within the container shape, or the container shape’s corners have different radii. When you provide `true` for `isUniform`, the system calculates the radius for each corner first. Then, it selects the largest radius and applies it to each corner to achieve the symmetric look.

## Parameters

- `corners`: The corner style for all four corners.
- `isUniform`: A Boolean value that indicates whether to apply the corner style on each corner individually or uniformly.

## See Also

- [init(corners: Edge.Corner.Style, isUniform: Bool)](concentricrectangle/init(corners:isuniform:).md)
  Creates a rectangle with the same corner style set on four corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(corners:isuniform:))*