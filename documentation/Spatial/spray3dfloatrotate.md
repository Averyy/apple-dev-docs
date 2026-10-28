# SPRay3DFloatRotate

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
static SPRay3DFloat SPRay3DFloatRotate(SPRay3DFloat ray, SPRotation3DFloat rotation);
```

## Return Value

A ray with a direction that’s rotated by the specified quaternion.

## Discussion

Returns a ray that’s rotated by the specified rotation.

## Parameters

- `ray`: The source ray.
- `rotation`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dfloatrotate)*