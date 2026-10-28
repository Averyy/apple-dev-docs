# SPPose3DFloatAlmostEqualToPose

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
static bool SPPose3DFloatAlmostEqualToPose(SPPose3DFloat p1, SPPose3DFloat p2);
```

## Return Value

A Boolean value that indicates whether the two pose’s matrices are equal within the Spatial default absolute tolerance.

## Discussion

Returns a Boolean value that indicates whether the two poses’s matrices are equal within the Spatial default absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `p1`: The first pose.
- `p2`: The first pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatalmostequaltopose-5t5q)*