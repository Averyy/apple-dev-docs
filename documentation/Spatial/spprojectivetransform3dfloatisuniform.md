# SPProjectiveTransform3DFloatIsUniform

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
static bool SPProjectiveTransform3DFloatIsUniform(SPProjectiveTransform3DFloat transform);
```

## Return Value

A Boolean value that indicates whether the transform is affine and uniform over all dimensions.

## Discussion

Returns a Boolean value that indicates whether the transform is affine and scales equally over all dimensions.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatisuniform)*