# SPPoint3DIsNaN

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
static bool SPPoint3DIsNaN(SPPoint3D point);
```

#### Return Value

A Boolean value that indicates whether the point contains any NaN values.

#### Discussion

Returns a Boolean value that indicates whether the point contains any NaN values.

## Parameters

- `point`: The source point.

## See Also

### Checking characteristics
- [func distance(to: Point3D) -> Double](./point3d/distance%28to%29.md)
  Returns the distance between two points.
- [SPPoint3DIsFinite](./sppoint3disfinite.md)
- [SPPoint3DIsZero](./sppoint3diszero.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3disnan)*