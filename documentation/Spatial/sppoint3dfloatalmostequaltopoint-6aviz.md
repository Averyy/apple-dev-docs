# SPPoint3DFloatAlmostEqualToPoint

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
static bool SPPoint3DFloatAlmostEqualToPoint(SPPoint3DFloat p1, SPPoint3DFloat p2, float tolerance);
```

## Return Value

A Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.

## Discussion

Returns a Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `p1`: The first point.
- `p2`: The first point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatalmostequaltopoint-6aviz)*