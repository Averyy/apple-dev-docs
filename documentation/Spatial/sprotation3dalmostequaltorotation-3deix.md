# SPRotation3DAlmostEqualToRotation

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
static bool SPRotation3DAlmostEqualToRotation(SPRotation3D r1, SPRotation3D r2, double tolerance);
```

#### Return Value

A Boolean value that indicates whether the two rotations are equal within the specified absolute tolerance.

## Parameters

- `r1`: The first rotation.
- `r2`: The second rotation.
- `tolerance`: How close the two rotations must be to be considered “almost equal”.

## See Also

### Comparing values
- [SPRotation3DEqualToRotation](./sprotation3dequaltorotation.md)
  Returns a Boolean value that indicates whether two values are equal.
- [SPRotation3DAlmostEqualToRotation](./sprotation3dalmostequaltorotation-53c20.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dalmostequaltorotation-3deix)*