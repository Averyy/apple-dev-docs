# Audio.Directivity

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The radiation pattern of sound emitted from an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum Directivity
```

## Topics

### Enumeration Cases
- [Audio.Directivity.beam(focus:)](./directivity/beam%28focus%29.md)
  A parametric frequency-dependent radiation pattern, where the `focus` determines the width of a beam.

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
- [Audio.DistanceAttenuation](./distanceattenuation.md)
  The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/directivity)*