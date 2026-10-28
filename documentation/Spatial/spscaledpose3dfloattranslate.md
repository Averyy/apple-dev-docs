# SPScaledPose3DFloatTranslate

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
static SPScaledPose3DFloat SPScaledPose3DFloatTranslate(SPScaledPose3DFloat scaledPose, SPVector3DFloat offset);
```

## Return Value

A scaled pose that’s offset by the @p x, @p y, and @p z of the vector.

## Discussion

Returns a scaled pose with a position that is offset from that of the source scaled pose.

## Parameters

- `scaledPose`: The source scaled pose.
- `offset`: A vector that defines the offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloattranslate)*