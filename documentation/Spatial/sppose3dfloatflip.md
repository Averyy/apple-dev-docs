# SPPose3DFloatFlip

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
static SPPose3DFloat SPPose3DFloatFlip(SPPose3DFloat pose, SPAxis flipAxis);
```

#### Return Value

A new pose flipped along the specified axis.

#### Discussion

Returns a pose that’s flipped along the specified axis.

If you pass a flip axis that’s not @p x , @p y , or @p z , the function returns @p pose unmodified.

## Parameters

- `pose`: The source pose.
- `flipAxis`: The flip axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatflip)*