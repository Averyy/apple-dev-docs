# infinite()

**Framework**: SpriteKit  
**Kind**: method

Returns a region that defines a region that includes all points.

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
class func infinite() -> Self
```

#### Return Value

Returns a singleton region that covers an infinite area.

## See Also

- [init(size: CGSize)](skregion/init(size:).md)
  Initializes a new region with a rectangular area.
- [init(radius: Float)](skregion/init(radius:).md)
  Initializes a new region with a circular area.
- [init(path: CGPath)](skregion/init(path:).md)
  Initializes a new region using a Core Graphics path.
- [func inverse() -> Self](skregion/inverse.md)
  Returns a new region that is the mathematical inverse of an existing region.
- [func byDifference(from: SKRegion) -> Self](skregion/bydifference(from:).md)
  Returns a new region created by subtracting the contents of another region from this region.
- [func byIntersection(with: SKRegion) -> Self](skregion/byintersection(with:).md)
  Returns a new region created by intersecting the contents of this region with another region.
- [func byUnion(with: SKRegion) -> Self](skregion/byunion(with:).md)
  Returns a new region created by combining the contents of this region with another region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion/infinite())*