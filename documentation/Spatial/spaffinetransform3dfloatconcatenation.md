# SPAffineTransform3DFloatConcatenation

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatConcatenation(SPAffineTransform3DFloat t1, SPAffineTransform3DFloat t2);
```

#### Return Value

An affine transformation matrix that’s constructed by concatenating two existing affine transforms.

#### Discussion

Returns an affine transformation matrix that’s constructed by concatenating two existing affine transforms.

## Parameters

- `t1`: The first transform.
- `t2`: The second transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatconcatenation)*