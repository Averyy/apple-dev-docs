# SPProjectiveTransform3DFloatTranslate

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
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatTranslate(SPProjectiveTransform3DFloat transform, SPVector3DFloat offset);
```

#### Return Value

A transform that’s offset by the @p width, @p height, and @p depth of the size.

#### Discussion

Returns a projective transform that’s constructed by concatenating an existing projective transform and a translation.

## Parameters

- `transform`: The source transform.
- `offset`: A vector that defines the translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloattranslate)*