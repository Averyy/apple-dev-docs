# SPRect3DFloatUnapplyScaledPose

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
static SPRect3DFloat SPRect3DFloatUnapplyScaledPose(SPRect3DFloat rect, SPScaledPose3DFloat pose);
```

## Return Value

The transformed rectangle.

## Discussion

Returns a rectangle that’s transformed by the inverse of the specified scaled pose.

> **Note**: The pose’s rotation angle must be zero, otherwise this function returns @p SPRect3DFloatNull .

## Parameters

- `rect`: The source rectangle.
- `pose`: The scaled pose that the function unapplies to the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatunapplyscaledpose)*