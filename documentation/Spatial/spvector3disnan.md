# SPVector3DIsNaN

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
static bool SPVector3DIsNaN(SPVector3D vector);
```

#### Return Value

A Boolean value that indicates whether the point contains any NaN values.

#### Discussion

Returns a Boolean value that indicates whether the vector contains any NaN values.

## Parameters

- `vector`: The source point.

## See Also

### Checking characteristics
- [SPVector3DRotationToVector](./spvector3drotationtovector.md)
  Returns the rotation around the origin from the first vector to the second vector.
- [SPVector3DIsZero](./spvector3diszero.md)
- [SPVector3DIsFinite](./spvector3disfinite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3disnan)*