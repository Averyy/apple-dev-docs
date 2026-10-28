# SPProjectiveTransform3DFloatFlip

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
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatFlip(SPProjectiveTransform3DFloat transform, SPAxis flipAxis);
```

## Return Value

A new transform flipped along the specified axis.

## Discussion

Returns a projective transform that’s flipped along the specified axis.

> **Note**: The transform must be affine, otherwise the function returns @p SPProjectiveTransform3DFloatInvalid .

If you pass a shear axis that’s not @p x , @p y , or @p z , the function returns @p transform unmodified.

## Parameters

- `flipAxis`: The flip axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatflip)*