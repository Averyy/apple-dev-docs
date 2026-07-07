# withParticleIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the indices of particles that collided with the collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withParticleIndices<Result>(_ callback: (Span<UInt32>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

This span is only available during the subscription callback of this event. The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the colliding particle indices.

## See Also

- [var particleIndices: Span<UInt32>](clothcolliderevents/newbodycollisions/collision/particleindices.md)
  The indices of particles that collided with the collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/collision/withparticleindices(_:))*