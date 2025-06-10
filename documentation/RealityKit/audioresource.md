# AudioResource

**Framework**: RealityKit  
**Kind**: class

A playable audio resource

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
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
- [AudioResource.Calibration](audioresource/calibration-5a1sg.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Calibration](audioresource/calibration-89r8s.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization-3mh5o.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.
- [AudioResource.Normalization](audioresource/normalization-5mic7.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource)*