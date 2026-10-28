# SPRay3DFloatApplyProjectiveTransform

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
static SPRay3DFloat SPRay3DFloatApplyProjectiveTransform(SPRay3DFloat ray, SPProjectiveTransform3DFloat transform);
```

## Return Value

The transformed ray.

## Discussion

Returns a ray that’s transformed by the specified projective transform.

## Parameters

- `ray`: The source ray.
- `transform`: The projective transform that the function applies to the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dfloatapplyprojectivetransform)*