# SPPoint3DFloatUnapplyPose

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
static SPPoint3DFloat SPPoint3DFloatUnapplyPose(SPPoint3DFloat point, SPPose3DFloat pose);
```

## Return Value

The transformed point.

## Discussion

Returns a point that’s transformed by the inverse of the specified pose.

## Parameters

- `point`: The source point.
- `pose`: The pose that the function unapplies to the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatunapplypose)*