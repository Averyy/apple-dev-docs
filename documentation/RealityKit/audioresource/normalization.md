# AudioResource.Normalization

**Framework**: RealityKit  
**Kind**: struct

Normalization adjusts the level of an audio file or buffer to be at a defined target.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Normalization
```

#### Overview

Audio files produced in a production environment where dynamics are already being processed may not need normalization.

Normalization has a CPU cost on  for audio file resources that have a loading strategy of [`AudioFileResource.LoadingStrategy.preload`](audiofileresource/loadingstrategy-swift.enum/preload.md) and a CPU cost on  for audio files that have a loading strategy of [`AudioFileResource.LoadingStrategy.stream`](audiofileresource/loadingstrategy-swift.enum/stream.md).

## Topics

### Type Properties
- [static let dynamic: AudioResource.Normalization](audioresource/normalization/dynamic.md)
  Performs dynamic compression to normalize the audio source material to a level of -12dBLUFS in real-time.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/normalization)*