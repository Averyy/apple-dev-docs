# SPRect3DFloatUnapplyPose

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
static SPRect3DFloat SPRect3DFloatUnapplyPose(SPRect3DFloat rect, SPPose3DFloat pose);
```

#### Return Value

The transformed rectangle.

#### Discussion

Returns a rectangle that’s transformed by the inverse of the specified pose.

> **Note**: The pose’s rotation angle must be zero, otherwise this function returns @p SPRect3DFloatNull .

## Parameters

- `rect`: The source rectangle.
- `pose`: The pose that the function unapplies to the size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatunapplypose)*