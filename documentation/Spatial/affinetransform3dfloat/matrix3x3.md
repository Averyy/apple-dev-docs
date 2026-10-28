# matrix3x3

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

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
var matrix3x3: simd_float3x3 { get }
```

```c
static simd_float3x3 SPAffineTransform3DFloatGet3x3Matrix(SPAffineTransform3DFloat transform);
```

## Discussion

Returns the first three columns of an affine transform’s underlying matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/matrix3x3)*