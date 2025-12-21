# isUniform(overDimensions:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Returns `true` if the transform is uniform over the specified dimensions.

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
func isUniform(overDimensions: Dimension3DSet) -> Bool
```

#### Discussion

If you specify `overDimensions` as `Dimension3DSet.all`, the function returns the same result as `Transform3D.getter:isUniform`. If you specify as `overDimensions` with zero or one dimension, the function returns the same result as `Transform3D.getter:isRectilinear`.

## Parameters

- `overDimensions`: The dimensions that the function tests are uniform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/transform3dprotocol/isuniform(overdimensions:))*