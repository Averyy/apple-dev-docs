# SPVector3DRotationToVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the rotation around the origin from the first vector to the second vector.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPRotation3D SPVector3DRotationToVector(SPVector3D vector, SPVector3D other);
```

#### Return Value

The rotation between two vector.

## Parameters

- `vector`: The first vector that the function computes the rotation from.
- `other`: The second vector that the function computes the rotation to.

## See Also

### Checking characteristics
- [SPVector3DIsZero](./spvector3diszero.md)
- [SPVector3DIsFinite](./spvector3disfinite.md)
- [SPVector3DIsNaN](./spvector3disnan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3drotationtovector)*