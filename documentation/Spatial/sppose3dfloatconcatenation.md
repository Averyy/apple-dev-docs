# SPPose3DFloatConcatenation

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
static SPPose3DFloat SPPose3DFloatConcatenation(SPPose3DFloat lhs, SPPose3DFloat rhs);
```

#### Return Value

A new pose structure.

#### Discussion

Returns a new pose that’s constructed by concatenating two existing  poses.

## Parameters

- `lhs`: The first pose to multiply.
- `rhs`: The second pose to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatconcatenation)*