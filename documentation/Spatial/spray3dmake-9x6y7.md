# SPRay3DMake

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
static SPRay3D SPRay3DMake(SPPoint3D origin, SPVector3D direction);
```

## Return Value

A new ray stucture.

## Discussion

Returns a ray at the specified origin.

> **Note**: This function normalizes nonzero direction vectors.

## Parameters

- `origin`: A point structure that specifies the origin of the ray.
- `direction`: A Spatial vector that specifies the direction of the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dmake-9x6y7)*