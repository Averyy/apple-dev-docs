# byIntersection(with:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns a new region created by intersecting the contents of this region with another region.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func byIntersection(with region: SKRegion) -> Self
```

```objc
- (instancetype) regionByIntersectionWithRegion:(SKRegion *) region;
```

## Return Value

A new region whose contents include all points that are included in both regions.

## Parameters

- `region`: The region to intersect.

## See Also

### Creating and Initializing Region Objects
- [class func infinite() -> Self](./infinite%28%29.md)
  Returns a region that defines a region that includes all points.
- [init(size: CGSize)](./init%28size%29.md)
  Initializes a new region with a rectangular area.
- [init(radius: Float)](./init%28radius%29.md)
  Initializes a new region with a circular area.
- [init(path: CGPath)](./init%28path%29.md)
  Initializes a new region using a Core Graphics path.
- [func inverse() -> Self](./inverse%28%29.md)
  Returns a new region that is the mathematical inverse of an existing region.
- [func byDifference(from: SKRegion) -> Self](./bydifference%28from%29.md)
  Returns a new region created by subtracting the contents of another region from this region.
- [func byUnion(with: SKRegion) -> Self](./byunion%28with%29.md)
  Returns a new region created by combining the contents of this region with another region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion/byintersection(with:))*