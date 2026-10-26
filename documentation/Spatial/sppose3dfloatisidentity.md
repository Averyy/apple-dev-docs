# SPPose3DFloatIsIdentity

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
static bool SPPose3DFloatIsIdentity(SPPose3DFloat pose);
```

#### Return Value

A Boolean value that indicates whether the transform is the identity transform.

#### Discussion

Returns a Boolean value that indicates whether the pose is the identity transform.

> **Note**: This function checks for equality within the Spatial default tolerance.

## Parameters

- `pose`: The source pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatisidentity)*