# SPScaledPose3DFloatIsIdentity

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
static bool SPScaledPose3DFloatIsIdentity(SPScaledPose3DFloat scaledPose);
```

#### Return Value

A Boolean value that indicates whether the transform is the identity pose.

#### Discussion

Returns a Boolean value that indicates whether the scaled pose is the identity transform.

> **Note**: This function checks for equality within the Spatial default tolerance.

## Parameters

- `scaledPose`: The source scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatisidentity)*