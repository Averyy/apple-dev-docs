# SPAffineTransform3DFloatShear

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatShear(SPAffineTransform3DFloat transform, SPAxis shearAxis, float shearFactor0, float shearFactor1);
```

## Return Value

The transformed transform.

## Discussion

Returns an affine transform that’s sheared over an axis by shear factors for the other two axes.

When the shear axis is @p x , @p shearFactor0 is the @p y shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p y , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p z shear factor.

When the shear axis is @p z , @p shearFactor0 is the @p x  shear factor and @p shearFactor0 is the @p y shear factor.

If you pass a shear axis that’s not @p x , @p y , or @p z , the function returns @p transform unmodified.

## Parameters

- `transform`: The source transform.
- `shearAxis`: The shear axis.
- `shearFactor0`: The first shear factor.
- `shearFactor1`: The second shear factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatshear)*