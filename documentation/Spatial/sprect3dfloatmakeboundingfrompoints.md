# SPRect3DFloatMakeBoundingFromPoints

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
static SPRect3DFloat SPRect3DFloatMakeBoundingFromPoints(SPPoint3DFloat points[], int pointCount);
```

#### Return Value

A new rectangle stucture.

#### Discussion

Returns a rectangle that’s the bounding box of the specified points.

## Parameters

- `points`: The source points.
- `pointCount`: The number of points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatmakeboundingfrompoints)*