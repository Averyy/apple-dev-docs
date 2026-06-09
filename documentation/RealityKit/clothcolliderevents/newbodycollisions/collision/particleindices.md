# particleIndices

**Framework**: RealityKit  
**Kind**: property

The indices of particles that collided with the collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var particleIndices: Span<UInt32> { get }
```

#### Discussion

The lifetime of this span is tied to the owning event, and thus cannot escape it. This data is only available during the subscription callback in which the owning event is provided. If you store the event and attempt to access this data after the subscription callback, then you will get an empty span instead.

## See Also

- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothcolliderevents/newbodycollisions/collision/withparticleindices(_:).md)
  Provides access to the indices of particles that collided with the collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/collision/particleindices)*