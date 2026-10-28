# byDifference(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new region created by subtracting the specified region from the current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func byDifference(from region: UIRegion) -> Self
```

```objc
- (instancetype) regionByDifferenceFromRegion:(UIRegion *) region;
```

## Return Value

A new region that contains the points that are in the current region and not in the area defined by the `region` parameter.

## Parameters

- `region`: The region to be subtracted from the current region.

## See Also

### Creating complex regions
- [func inverse() -> Self](./inverse%28%29.md)
  Returns a new region that’s the mathematical inverse of the current region.
- [func byIntersection(with: UIRegion) -> Self](./byintersection%28with%29.md)
  Returns a new region containing only the area occupied by both the specified region and current region.
- [func byUnion(with: UIRegion) -> Self](./byunion%28with%29.md)
  Returns a new region containing the combined areas of the specified region and the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/bydifference(from:))*