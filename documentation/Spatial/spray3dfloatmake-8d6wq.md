# SPRay3DFloatMake

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
static SPRay3DFloat SPRay3DFloatMake(SPPoint3DFloat origin, SPVector3DFloat direction);
```

#### Return Value

A new ray stucture.

#### Discussion

Returns a ray at the specified origin.

> **Note**: This function normalizes nonzero direction vectors.

## Parameters

- `origin`: A point structure that specifies the origin of the ray.
- `direction`: A Spatial vector that specifies the direction of the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dfloatmake-8d6wq)*