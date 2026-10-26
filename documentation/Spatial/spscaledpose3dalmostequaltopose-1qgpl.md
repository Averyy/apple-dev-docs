# SPScaledPose3DAlmostEqualToPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static bool SPScaledPose3DAlmostEqualToPose(SPScaledPose3D p1, SPScaledPose3D p2);
```

#### Return Value

A Boolean value that indicates whether the two scaled poses are equal within the Spatial default absolute tolerance.

#### Discussion

Returns a Boolean value that indicates whether the two scaled poses are equal within the Spatial default absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `p1`: The first scaled pose.
- `p2`: The first scaled pose.

## See Also

### Comparing values
- [SPScaledPose3DAlmostEqualToPose](./spscaledpose3dalmostequaltopose-4ahe1.md)
  Returns a Boolean value that indicates whether the two scaled poses are equal within the specified absolute tolerance.
- [SPScaledPose3DEqualToPose](./spscaledpose3dequaltopose.md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dalmostequaltopose-1qgpl)*