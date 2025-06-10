# Audio.Directivity

**Framework**: RealityKit  
**Kind**: enum

The radiation pattern of sound emitted from an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
enum Directivity
```

## Topics

### Enumeration Cases
- [Audio.Directivity.beam(focus:)](audio/directivity/beam(focus:).md)
  A parametric frequency-dependent radiation pattern, where the `focus` determines the width of a beam.

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
- [Audio.DistanceAttenuation](audio/distanceattenuation.md)
  The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/directivity)*