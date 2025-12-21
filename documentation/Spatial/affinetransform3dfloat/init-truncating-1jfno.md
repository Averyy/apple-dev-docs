# init(truncating:)

**Framework**: Spatial  
**Kind**: init

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
init(truncating transform: ProjectiveTransform3DFloat)
```

#### Return Value

A new affine transform structure.

#### Discussion

Returns a new affine transform structure from the first three rows of the specified projective transform.

> **Note**: This function is similar to @p SPAffineTransform3DFloatMakeWithProjective, but it ignores the last row of the matrix.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/init(truncating:)-1jfno)*