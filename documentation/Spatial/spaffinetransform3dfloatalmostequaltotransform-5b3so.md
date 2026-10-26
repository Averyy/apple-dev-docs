# SPAffineTransform3DFloatAlmostEqualToTransform

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
static bool SPAffineTransform3DFloatAlmostEqualToTransform(SPAffineTransform3DFloat t1, SPAffineTransform3DFloat t2, float tolerance);
```

#### Return Value

A Boolean value that indicates whether the two transform’s matrices are equal within the specified absolute tolerance.

#### Discussion

Returns a Boolean value that indicates whether the two transform’s matrices are equal within the specified absolute tolerance.

## Parameters

- `t1`: The first transform.
- `t2`: The first transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatalmostequaltotransform-5b3so)*