# SPVector3DFloatLerp

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
static SPVector3DFloat SPVector3DFloatLerp(SPVector3DFloat from, SPVector3DFloat to, SPVector3DFloat t);
```

## Return Value

A new rotation. When @p t=0, the result is the @p from vector. When @p t=1.0, the result is the @p to vector. For any other value of @p t, the result is a linear linear interpolation between the two vectors.

## Discussion

Returns a Spatial vector that represents the linear interpolation at @p t between two vectors.

## Parameters

- `from`: The starting vector.
- `to`: The ending vector.
- `t`: The value, between @p 0 and @p 1, that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dfloatlerp)*