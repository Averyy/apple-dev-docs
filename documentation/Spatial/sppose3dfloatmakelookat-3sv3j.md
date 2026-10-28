# SPPose3DFloatMakeLookAt

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
static SPPose3DFloat SPPose3DFloatMakeLookAt(SPPoint3DFloat position, SPPoint3DFloat target, SPVector3DFloat up);
```

## Return Value

A new pose structure.

## Discussion

Returns a pose at the specified position with the rotation towards the target.

## Parameters

- `position`: A point structure that specifies the position of the pose.
- `target`: The point that the pose orients towards.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatmakelookat-3sv3j)*