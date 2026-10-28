# SPRay3DFloatUnapplyAffineTransform

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
static SPRay3DFloat SPRay3DFloatUnapplyAffineTransform(SPRay3DFloat ray, SPAffineTransform3DFloat transform);
```

## Return Value

The transformed ray.

## Discussion

Returns a ray that’s transformed by the inverse of the specified affine transform.

## Parameters

- `ray`: The source ray.
- `transform`: The affine transform that the function unapplies to the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dfloatunapplyaffinetransform)*