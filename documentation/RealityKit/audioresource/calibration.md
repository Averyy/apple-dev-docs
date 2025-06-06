# AudioResource.Calibration

**Framework**: RealityKit  
**Kind**: struct

A container for different calibration modes that can be applied for playback.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Calibration
```

## Topics

### Type Methods
- [static func absolute(dBSPL: Audio.Decibel) -> AudioResource.Calibration](audioresource/calibration/absolute(dbspl:).md)
  The reference level (-12dBLUFS) of the audio source material will be reproduced at the given `dBSPL` level on known audio output hardware.
- [static func relative(dBSPL: Audio.Decibel) -> AudioResource.Calibration](audioresource/calibration/relative(dbspl:).md)
  Relative adjustment of the resource from the default level of the audio output hardware.
### Default Implementations
- [Equatable Implementations](audioresource/calibration/equatable-implementations.md)
- [Hashable Implementations](audioresource/calibration/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AudioFileResource](audiofileresource.md)
  An audio resource that you load from a file or from a URL.
- [class AudioFileGroupResource](audiofilegroupresource.md)
  An audio file group.
- [class AudioBufferResource](audiobufferresource.md)
  An audio resource that you load from an [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer).
- [struct AudioLibraryComponent](audiolibrarycomponent.md)
  A container for audio resources that you can look up by user-defined names.
- [class AudioResource](audioresource.md)
  A playable audio resource
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/calibration)*