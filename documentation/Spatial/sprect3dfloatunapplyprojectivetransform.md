# SPRect3DFloatUnapplyProjectiveTransform

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
static SPRect3DFloat SPRect3DFloatUnapplyProjectiveTransform(SPRect3DFloat rect, SPProjectiveTransform3DFloat transform);
```

## Return Value

The transformed rectangle.

## Discussion

Returns a rectangle that’s transformed by the inverse of the specified projective transform.

> **Note**: The transform must be rectilinear otherwise this function returns @p SPRect3DFloatNull .

## Parameters

- `rect`: The source rectangle.
- `transform`: The projective transform that the function unapplies to the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatunapplyprojectivetransform)*