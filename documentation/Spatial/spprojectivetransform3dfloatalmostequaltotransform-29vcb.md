# SPProjectiveTransform3DFloatAlmostEqualToTransform

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
static bool SPProjectiveTransform3DFloatAlmostEqualToTransform(SPProjectiveTransform3DFloat t1, SPProjectiveTransform3DFloat t2);
```

## Return Value

A Boolean value that indicates whether the two transform’s matrices are equal within the Spatial default absolute tolerance.

## Discussion

Returns a Boolean value that indicates whether the two transform’s matrices are equal within the Spatial default absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `t1`: The first transform.
- `t2`: The first transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatalmostequaltotransform-29vcb)*