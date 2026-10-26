# SPProjectiveTransform3DFloatMakeShear

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
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatMakeShear(SPAxis shearAxis, float shearFactor0, float shearFactor1);
```

#### Return Value

A new affine transform structure.

#### Discussion

Returns a new shear affine transform.

When the shear axis is @p x , @p shearFactor0 is the @p y shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p y , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p z , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p y shear factor.

## Parameters

- `shearAxis`: The shear axis.
- `shearFactor0`: The first shear factor.
- `shearFactor1`: The second shear factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatmakeshear)*