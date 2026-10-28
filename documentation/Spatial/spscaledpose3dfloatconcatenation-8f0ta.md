# SPScaledPose3DFloatConcatenation

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
static SPScaledPose3DFloat SPScaledPose3DFloatConcatenation(SPPose3DFloat lhs, SPScaledPose3DFloat rhs);
```

## Return Value

A new pose structure.

## Discussion

Returns a new scaled pose that’s constructed by concatenating a pose and a scaled pose.

## Parameters

- `lhs`: The first pose to multiply.
- `rhs`: The second scaled pose to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatconcatenation-8f0ta)*