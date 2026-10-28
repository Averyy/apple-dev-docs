# SPVector3DFloatShear

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
static SPVector3DFloat SPVector3DFloatShear(SPVector3DFloat vector, SPAxis shearAxis, float shearFactor0, float shearFactor1);
```

## Return Value

The transformed vector.

## Discussion

Returns a vector that’s sheared over an axis by shear factors for the other two axes.

When the shear axis is @p x , @p shearFactor0 is the @p y shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p y , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p z , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p y shear factor.

## Parameters

- `vector`: The source vector.
- `shearAxis`: The shear axis.
- `shearFactor0`: The first shear factor.
- `shearFactor1`: The second shear factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dfloatshear)*