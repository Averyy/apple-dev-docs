# SPProjectiveTransform3DFloatRotate

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
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatRotate(SPProjectiveTransform3DFloat transform, SPRotation3DFloat rotation);
```

#### Return Value

A transform that’s rotated by the specified rotation.

#### Discussion

Returns a projective transform that’s constructed by concatenating an existing projective transform and a rotation.

## Parameters

- `transform`: The source transform.
- `rotation`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatrotate)*