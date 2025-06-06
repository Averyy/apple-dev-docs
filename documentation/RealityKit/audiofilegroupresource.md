# AudioFileGroupResource

**Framework**: RealityKit  
**Kind**: class

An audio file group.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency class AudioFileGroupResource
```

## Topics

### Creating a resource
- [init([AudioFileResource]) throws](audiofilegroupresource/init(_:).md)
  Creates a group resource from an array of audio file resources.
- [convenience init(named: String, from: String, in: Bundle) async throws](audiofilegroupresource/init(named:from:in:).md)
  Initializes an audio resource from a Reality Composer Pro project.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileGroupResource](audiofilegroupresource/load(named:from:in:).md)
  Loads an audio resource from a Reality Composer Pro project.
### Working with the resource contents
- [let resources: [AudioFileResource]](audiofilegroupresource/resources.md)
  The `AudioFileResource` objects which comprise this `AudioFileGroupResource`.
- [static func == (AudioFileGroupResource, AudioFileGroupResource) -> Bool](audiofilegroupresource/==(_:_:).md)
### Default Implementations
- [Hashable Implementations](audiofilegroupresource/hashable-implementations.md)

## Relationships

### Inherits From
- [AudioResource](audioresource.md)
### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AudioFileResource](audiofileresource.md)
  An audio resource that you load from a file or from a URL.
- [class AudioBufferResource](audiobufferresource.md)
  An audio resource that you load from an [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer).
- [struct AudioLibraryComponent](audiolibrarycomponent.md)
  A container for audio resources that you can look up by user-defined names.
- [class AudioResource](audioresource.md)
  A playable audio resource
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource)*