# init(truncating:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

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
init(truncating matrix: simd_float4x4)
```

```c
static SPAffineTransform3DFloat SPAffineTransform3DFloatMakeWithTruncated4x4Matrix(simd_float4x4 matrix);
```

#### Return Value

A new affine transform structure.

#### Discussion

Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.

## Parameters

- `matrix`: The source matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/init(truncating:)-8jfn6)*