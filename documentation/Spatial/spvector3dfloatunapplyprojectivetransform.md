# SPVector3DFloatUnapplyProjectiveTransform

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
static SPVector3DFloat SPVector3DFloatUnapplyProjectiveTransform(SPVector3DFloat vector, SPProjectiveTransform3DFloat transform);
```

#### Return Value

The transformed vector.

#### Discussion

Returns a vector that’s transformed by the inverse of the specified projective transform.

## Parameters

- `vector`: The source vector.
- `transform`: The projective transform whose inverse is to be applied to the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dfloatunapplyprojectivetransform)*