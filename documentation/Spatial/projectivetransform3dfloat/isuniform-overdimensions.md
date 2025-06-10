# isUniform(overDimensions:)

**Framework**: Spatial  
**Kind**: method

Returns `true` if the transform is affine and uniform over the specified dimensions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func isUniform(overDimensions: Dimension3DSet) -> Bool
```

#### Discussion

If you specify `overDimensions` as `Dimension3DFloatSet.all`, the function returns the same result as `Transform3DFloat.getter:isUniform`. If you specify as `overDimensions` with zero or one dimension, the function returns the same result as `Transform3DFloat.getter:isRectilinear`.

## Parameters

- `overDimensions`: The dimensions that the function tests are uniform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/isuniform(overdimensions:))*