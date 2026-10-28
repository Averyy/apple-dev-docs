# byIntersection(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new region containing only the area occupied by both the specified region and current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func byIntersection(with region: UIRegion) -> Self
```

```objc
- (instancetype) regionByIntersectionWithRegion:(UIRegion *) region;
```

## Return Value

A new region that contains only the points that are in both the current region and the shape specified by the `region` parameter.

## Parameters

- `region`: The region to be intersected with the current region.

## See Also

### Creating complex regions
- [func inverse() -> Self](./inverse%28%29.md)
  Returns a new region that’s the mathematical inverse of the current region.
- [func byDifference(from: UIRegion) -> Self](./bydifference%28from%29.md)
  Returns a new region created by subtracting the specified region from the current region.
- [func byUnion(with: UIRegion) -> Self](./byunion%28with%29.md)
  Returns a new region containing the combined areas of the specified region and the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/byintersection(with:))*