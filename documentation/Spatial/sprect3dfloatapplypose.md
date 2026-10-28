# SPRect3DFloatApplyPose

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
static SPRect3DFloat SPRect3DFloatApplyPose(SPRect3DFloat rect, SPPose3DFloat pose);
```

## Return Value

The transformed rectangle.

## Discussion

Returns a rectangle that’s transformed by the specified pose.

## Parameters

- `rect`: The source rectangle.
- `pose`: The pose that the function applies to the size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatapplypose)*