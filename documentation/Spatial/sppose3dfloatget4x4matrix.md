# SPPose3DFloatGet4x4Matrix

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
static simd_float4x4 SPPose3DFloatGet4x4Matrix(SPPose3DFloat pose);
```

## Return Value

A new pose structure.

## Discussion

Returns a 4 x 4 matrix that represents the pose’s translation and rotation.

## Parameters

- `pose`: The source pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatget4x4matrix)*