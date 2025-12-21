# Audio.DistanceAttenuation

**Framework**: RealityKit  
**Kind**: enum

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
- [Audio.DistanceAttenuation.rolloff(factor:)](audio/distanceattenuation/rolloff(factor:).md)
  A standard geometric model for attenuating audio intensity naturally with distance, using a specified loss strength factor.
### Type Properties
- [static let `default`: Audio.DistanceAttenuation](audio/distanceattenuation/default.md)
  The default distance attenuation, which uses a rolloff model that mimics real-world physics.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [enum Audio](audio.md)
  A namespace for types that are used commonly in audio.
- [typealias Decibel](audio/decibel.md)
  The unit for measuring intensity of sound on a logarithmic scale.
- [Audio.Directivity](audio/directivity.md)
  The radiation pattern of sound emitted from an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/distanceattenuation)*