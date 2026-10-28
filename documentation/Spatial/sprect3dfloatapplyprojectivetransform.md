# SPRect3DFloatApplyProjectiveTransform

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
static SPRect3DFloat SPRect3DFloatApplyProjectiveTransform(SPRect3DFloat rect, SPProjectiveTransform3DFloat transform);
```

## Return Value

The transformed rectangle.

## Discussion

Returns a rectangle that’s transformed by the specified projective transform.

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter. If the affine transform `transform` consists solely of scaling and translation operations, then the returned rectangle coincides with the rectangle constructed from the eight transformed corners.

## Parameters

- `rect`: The source rectangle.
- `transform`: The projective transform that the function applies to the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatapplyprojectivetransform)*