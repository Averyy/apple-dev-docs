# SPAffineTransform3DFloatTranslate

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatTranslate(SPAffineTransform3DFloat transform, SPVector3DFloat offset);
```

#### Return Value

A transform that’s offset by the @p x, @p y, and @p z of the vector.

#### Discussion

Returns an affine transform that’s constructed by concatenating an existing affine transform and a translation.

## Parameters

- `transform`: The source transform.
- `offset`: A vector that defines the translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloattranslate)*