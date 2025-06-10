# init(truncating:)

**Framework**: Spatial  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(truncating transform: ProjectiveTransform3DFloat)
```

#### Return Value

A new affine transform structure.

#### Discussion

> **Note**: This function is similar to @p SPAffineTransform3DFloatMakeWithProjective, but it ignores the last row of the matrix.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/init(truncating:)-1jfno)*