# NINearbyObjectWorldTransformNotAvailable

**Framework**: Nearby Interaction  
**Kind**: var  
**Role**: Global Variable

A constant that indicates that the framework is unable to provide a world transform for a nearby object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```c
extern simd_float4x4 NINearbyObjectWorldTransformNotAvailable;
```

## Discussion

The framework returns this constant for [`worldTransformForObject:`](./nisession/worldtransformforobject_.md) when it fails to produce a transform for the given object.

## See Also

### Utilizing Camera Assistance
- [func setARSession(ARSession)](./nisession/setarsession%28_%29.md)
  Provides the framework with an existing AR session to use for Camera Assistance.
- [- worldTransformForObject:](./nisession/worldtransformforobject_.md)
  Returns a world transform to integrate a nearby object in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobjectworldtransformnotavailable)*