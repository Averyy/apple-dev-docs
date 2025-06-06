# byUnion(with:)

**Framework**: UIKit  
**Kind**: method

Returns a new region containing the combined areas of the specified region and the current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func byUnion(with region: UIRegion) -> Self
```

#### Return Value

A new region that contains the points from both the current region and the shape specified by the `region` parameter.

#### Discussion

Combining any region with the infinite region returns the infinite region.

## Parameters

- `region`: The region to be combined with the current region.

## See Also

- [func inverse() -> Self](uiregion/inverse.md)
  Returns a new region that’s the mathematical inverse of the current region.
- [func byDifference(from: UIRegion) -> Self](uiregion/bydifference(from:).md)
  Returns a new region created by subtracting the specified region from the current region.
- [func byIntersection(with: UIRegion) -> Self](uiregion/byintersection(with:).md)
  Returns a new region containing only the area occupied by both the specified region and current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/byunion(with:))*