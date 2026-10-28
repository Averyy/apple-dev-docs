# SPScaledPose3DFloatFlip

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
static SPScaledPose3DFloat SPScaledPose3DFloatFlip(SPScaledPose3DFloat scaledPose, SPAxis flipAxis);
```

## Return Value

A new scaled pose flipped along the specified axis.

## Discussion

Returns a scaled pose that’s flipped along the specified axis.

If you pass a flip axis that’s not @p x , @p y , or @p z , the function returns @p scaled pose unmodified.

> **Note**: The flipped scaled pose that this function returns has the same scale as the specified pose.

## Parameters

- `scaledPose`: The source scaled pose.
- `flipAxis`: The flip axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatflip)*