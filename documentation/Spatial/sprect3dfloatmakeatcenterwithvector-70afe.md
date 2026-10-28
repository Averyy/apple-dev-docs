# SPRect3DFloatMakeAtCenterWithVector

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
static SPRect3DFloat SPRect3DFloatMakeAtCenterWithVector(simd_float3 center, simd_float3 size);
```

## Return Value

A new rectangle stucture.

## Discussion

Returns a rectangle at the specified center using simd vectors.

## Parameters

- `center`: A three-element vector that specifies the center of the rectangle.
- `size`: A three-element vector that specifies the size of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatmakeatcenterwithvector-70afe)*