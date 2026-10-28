# SPScaledPose3DConcatenation

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
static SPScaledPose3D SPScaledPose3DConcatenation(SPPose3D lhs, SPScaledPose3D rhs);
```

## Return Value

A new pose structure.

## Discussion

Returns a new scaled pose that’s constructed by concatenating a pose and a scaled pose.

## Parameters

- `lhs`: The first pose to multiply.
- `rhs`: The second scaled pose to multiply.

## See Also

### Concatenating
- [SPScaledPose3DConcatenation](./spscaledpose3dconcatenation-3i5ch.md)
- [SPScaledPose3DConcatenation](./spscaledpose3dconcatenation-7ljg6.md)
  Returns a new scaled pose that’s constructed by concatenating two existing poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dconcatenation-94ryp)*