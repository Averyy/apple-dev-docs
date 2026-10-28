# init(path:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new region using a Core Graphics path.

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
init(path: CGPath)
```

```objc
- (instancetype) initWithPath:(CGPathRef) path;
```

## Return Value

A newly initialized region.

## Parameters

- `path`: A path that defines the new region’s shape. The path is assumed to use the even-odd winding rule.

## See Also

### Creating and Initializing Region Objects
- [class func infinite() -> Self](./infinite%28%29.md)
  Returns a region that defines a region that includes all points.
- [init(size: CGSize)](./init%28size%29.md)
  Initializes a new region with a rectangular area.
- [init(radius: Float)](./init%28radius%29.md)
  Initializes a new region with a circular area.
- [func inverse() -> Self](./inverse%28%29.md)
  Returns a new region that is the mathematical inverse of an existing region.
- [func byDifference(from: SKRegion) -> Self](./bydifference%28from%29.md)
  Returns a new region created by subtracting the contents of another region from this region.
- [func byIntersection(with: SKRegion) -> Self](./byintersection%28with%29.md)
  Returns a new region created by intersecting the contents of this region with another region.
- [func byUnion(with: SKRegion) -> Self](./byunion%28with%29.md)
  Returns a new region created by combining the contents of this region with another region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion/init(path:))*