# SPProjectiveTransform3DFloatIsUniformOverDimensions

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
static bool SPProjectiveTransform3DFloatIsUniformOverDimensions(SPProjectiveTransform3DFloat transform, SPAxis dimensionFlags);
```

## Return Value

@P true if the transform is affine, rectilinear, and the specified axes have equal scales.

## Discussion

Returns `true` if the transform is affine and scales equally over the specified dimensions.

Passing  @p dimensionFlags of @p SPAxisX|SPAxisY|SPAxisZ returns the same result as @p SPProjectiveTransform3DFloatIsUniform . Passing a @p dimensionFlags  that specifies zero or one axis returns the same result as @p SPProjectiveTransform3DFloatIsRectilinear .

## Parameters

- `transform`: The transform.
- `dimensionFlags`: A bitmask that specifies which dimensions the function queries. Use logical OR to combine axes .


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatisuniformoverdimensions)*