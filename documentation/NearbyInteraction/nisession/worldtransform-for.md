# worldTransform(for:)

**Framework**: Nearby Interaction  
**Kind**: method

Returns a world transform to integrate a nearby object in an AR experience.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func worldTransform(for object: NINearbyObject) -> simd_float4x4?
```

#### Return Value

A world transform in ARKit’s coordinate space.

#### Discussion

This [`ARKit`](https://developer.apple.com/documentation/ARKit) transform represents the given object’s position in the physical environment, if it’s available. Otherwise, this function returns `nil`.

With this transform, you can:

- Overlay 3D virtual content onto a camera-feed visualization where the nearby object resides in the physical environment, such as done by an AR app’s renderer.
- Play a 3D-spatial sound from the location of the nearby object, for example, by using [`PHASE`](https://developer.apple.com/documentation/PHASE).

## Parameters

- `object`: The object for which to calculate a world transform.

## See Also

- [func setARSession(ARSession)](nisession/setarsession(_:).md)
  Provides the framework with an existing AR session to use for Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/worldtransform(for:))*