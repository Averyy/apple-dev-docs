# SPVector3DIsFinite

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

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
static bool SPVector3DIsFinite(SPVector3D vector);
```

## Return Value

A Boolean value that indicates whether all of the coordinates of the point are finite.

## Discussion

Returns a Boolean value that indicates whether all of the elements of the vector are finite.

## Parameters

- `vector`: The source vector.

## See Also

### Checking characteristics
- [SPVector3DRotationToVector](./spvector3drotationtovector.md)
  Returns the rotation around the origin from the first vector to the second vector.
- [SPVector3DIsZero](./spvector3diszero.md)
- [SPVector3DIsNaN](./spvector3disnan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3disfinite)*