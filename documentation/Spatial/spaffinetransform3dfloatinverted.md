# SPAffineTransform3DFloatInverted

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPAffineTransform3DFloat SPAffineTransform3DFloatInverted(SPAffineTransform3DFloat transform);
```

## Return Value

A new transform that’s constructed by inverting an existing affine transform.

## Discussion

Returns a new transform that’s constructed by inverting an existing affine transform.

> **Note**: The source transform must be invertible, call @p SPAffineTransform3DFloatIsInvertible to test whether this is the case. If the source transform isn’t invertible, the function returns @p SPAffineTransform3DFloatInvalid .

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatinverted)*