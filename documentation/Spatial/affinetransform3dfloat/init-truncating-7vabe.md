# init(truncating:)

**Framework**: Spatial  
**Kind**: init

Returns a new affine transform from a double-precision 4 x 4 matrix truncated to a  4 x 3 matrix.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(truncating matrix: simd_double4x4)
```

#### Discussion

> **Note**: This function is provided as a convenience. All Spatial storage and calculations are single-precision.

## Parameters

- `matrix`: The source matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/init(truncating:)-7vabe)*