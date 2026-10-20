# Audio.DistanceAttenuation

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum DistanceAttenuation
```

## Topics

### Enumeration Cases
- [Audio.DistanceAttenuation.rolloff(factor:)](./distanceattenuation/rolloff%28factor%29.md)
  A standard geometric model for attenuating audio intensity naturally with distance, using a specified loss strength factor.
### Type Properties
- [static let `default`: Audio.DistanceAttenuation](./distanceattenuation/default.md)
  The default distance attenuation, which uses a rolloff model that mimics real-world physics.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Audio types
- [enum Audio](../audio.md)
  A namespace for types that are used commonly in audio.
- [typealias Decibel](./decibel.md)
  The unit for measuring intensity of sound on a logarithmic scale.
- [Audio.Directivity](./directivity.md)
  The radiation pattern of sound emitted from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/distanceattenuation)*