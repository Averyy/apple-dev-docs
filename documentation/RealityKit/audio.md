# Audio

**Framework**: RealityKit  
**Kind**: enum

A namespace for types that are used commonly in audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum Audio
```

## Topics

### Playing audio resources
- [static func playAudio([(AudioResource, Entity)]) throws -> AudioPlaybackGroupController](audio/playaudio(_:).md)
  Prepares and plays multiple audio resources for synchronized playback
- [static func playAudio([(AudioResource, Entity)], at: AVAudioTime) throws -> AudioPlaybackGroupController](audio/playaudio(_:at:).md)
  Prepares and plays multiple audio resources for synchronized playback at a specified time.
- [static func prepareAudio([(AudioResource, Entity)]) throws -> AudioPlaybackGroupController](audio/prepareaudio(_:).md)
  Prepares multiple audio resources for synchronized playback without starting them.
### Defining acoustic properties
- [struct Material](audio/material.md)
- [struct Absorption](audio/absorption.md)
- [struct Scattering](audio/scattering.md)
### Type Aliases
- [typealias Decibel](audio/decibel.md)
  The unit for measuring intensity of sound on a logarithmic scale.
- [typealias GeneratorRenderHandler](audio/generatorrenderhandler.md)
  A handler that generates real-time audio.
### Enumerations
- [Audio.Directivity](audio/directivity.md)
  The radiation pattern of sound emitted from an entity.
- [Audio.DistanceAttenuation](audio/distanceattenuation.md)
  The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.

## See Also

- [typealias Decibel](audio/decibel.md)
  The unit for measuring intensity of sound on a logarithmic scale.
- [Audio.Directivity](audio/directivity.md)
  The radiation pattern of sound emitted from an entity.
- [Audio.DistanceAttenuation](audio/distanceattenuation.md)
  The different ways that audio intensity diminishes as the distance between the listener and the sound source increases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio)*