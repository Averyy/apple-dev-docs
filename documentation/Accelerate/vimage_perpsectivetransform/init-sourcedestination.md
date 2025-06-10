# init(source:destination:)

**Framework**: Accelerate  
**Kind**: init

Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init?(source: vImage_PerpsectiveTransform.QuadrilateralPoints, destination: vImage_PerpsectiveTransform.QuadrilateralPoints)
```

## Parameters

- `source`: The four source points.
- `destination`: The four destination points.

## See Also

- [init()](vimage_perpsectivetransform/init.md)
  Creates a projective-transformation structure.
- [init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float, vx: Float, vy: Float, v: Float)](vimage_perpsectivetransform/init(a:b:c:d:tx:ty:vx:vy:v:).md)
  Creates a projective-transformation structure from the specified single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_perpsectivetransform/init(source:destination:))*