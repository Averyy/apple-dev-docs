# worldTransformForObject:

**Framework**: Nearby Interaction  
**Kind**: method  
**Role**: Instance Method

Returns a world transform to integrate a nearby object in an AR experience.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```objc
- (simd_float4x4) worldTransformForObject:(NINearbyObject *) object;
```

## Return Value

A world transform in ARKit’s coordinate space.

## Discussion

This [ARKit](../../ARKit/ARKit.md) transform represents the given object’s position in the physical environment, if it’s available. Otherwise, this function returns [`NINearbyObjectWorldTransformNotAvailable`](../ninearbyobjectworldtransformnotavailable.md).

With this transform, you can:

- Overlay 3D virtual content onto a camera-feed visualization where the nearby object resides in the physical environment, such as done by an AR app’s renderer.
- Play a 3D-spatial sound from the location of the nearby object, for example, by using [PHASE](../../PHASE/PHASE.md).

## Parameters

- `object`: The object for which to calculate a world transform.

## See Also

### Utilizing Camera Assistance
- [func setARSession(ARSession)](./setarsession%28_%29.md)
  Provides the framework with an existing AR session to use for Camera Assistance.
- [NINearbyObjectWorldTransformNotAvailable](../ninearbyobjectworldtransformnotavailable.md)
  A constant that indicates that the framework is unable to provide a world transform for a nearby object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/worldtransformforobject:)*