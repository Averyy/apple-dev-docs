# SPPose3DFloatTranslate

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
static SPPose3DFloat SPPose3DFloatTranslate(SPPose3DFloat pose, SPVector3DFloat offset);
```

#### Return Value

A pose that’s offset by the @p x, @p y, and @p z of the vector.

#### Discussion

Returns a pose with a position that is offset from that of the source pose.

## Parameters

- `pose`: The source pose.
- `offset`: A vector that defines the offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloattranslate)*