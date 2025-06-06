# AudioResource

**Framework**: RealityKit  
**Kind**: class

A playable audio resource

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class AudioResource
```

## Topics

### Deprecated
- [var inputMode: AudioResource.InputMode](audioresource/inputmode-swift.property.md)
- [AudioResource.InputMode](audioresource/inputmode-swift.enum.md)
### Structures
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.
### Default Implementations
- [Equatable Implementations](audioresource/equatable-implementations.md)

## Relationships

### Inherited By
- [AudioBufferResource](audiobufferresource.md)
- [AudioFileGroupResource](audiofilegroupresource.md)
- [AudioFileResource](audiofileresource.md)
### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Resource](resource.md)
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
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource)*