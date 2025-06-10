# AudioFileResource

**Framework**: RealityKit  
**Kind**: class

An audio resource that you load from a file or from a URL.

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
@preconcurrency class AudioFileResource
```

#### Overview

Load an audio file resource, like an audio file stored in .aiff or other format, by calling one of the load functions. Use the resource to create an [`AudioPlaybackController`](audioplaybackcontroller.md) instance by calling an entity’s [`prepareAudio(_:)`](entity/prepareaudio(_:).md) or [`playAudio(_:)`](entity/playaudio(_:).md) function. The controller plays the audio from the location in space of the entity that created the controller.

## Topics

### Loading audio from a bundle
- [convenience(named:from:in:)](audiofileresource/init(named:from:in:).md)
  Initializes a preconfigured AudioFileResource asynchronously from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.
- [convenience(named:in:configuration:)](audiofileresource/init(named:in:configuration:).md)
  Initializes an AudioFileResource asynchronously.
### Loading audio from a URL
- [convenience(contentsOf:withName:configuration:)](audiofileresource/init(contentsof:withname:configuration:).md)
  Initializes an AudioFileResource asynchronously.
### Describing the resource
- [let name: String](audiofileresource/name.md)
  The name of this `AudioFileResource`.
### Supporting types
- [AudioFileResource.LoadingStrategy](audiofileresource/loadingstrategy-swift.enum.md)
  A container for different strategies on how to handle resources’ data before and during playback.
### Deprecated
- [static func load(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(named:in:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func loadAsync(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](audiofileresource/loadasync(named:in:inputmode:loadingstrategy:shouldloop:).md)
- [static func load(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func loadAsync(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](audiofileresource/loadasync(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
- [var loadingStrategy: AudioFileResource.LoadingStrategy](audiofileresource/loadingstrategy-swift.property.md)
  The resource’s memory model.
- [var shouldLoop: Bool](audiofileresource/shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.
### Structures
- [AudioFileResource.Configuration](audiofileresource/configuration-461s2.md)
  A container for various settings for loading an audio file resource.
- [AudioFileResource.Configuration](audiofileresource/configuration-9pm1g.md)
  A container for various settings for loading an audio file resource.
### Operators
- [static ==(_:_:)](audiofileresource/==(_:_:).md)
### Instance Properties
- [let configuration: AudioFileResource.Configuration](audiofileresource/configuration-2jqgx.md)
  The configuration of this `AudioFileResource`.
- [let configuration: AudioFileResource.Configuration](audiofileresource/configuration-5rvk6.md)
  The configuration of this `AudioFileResource`.
- [var duration: Duration](audiofileresource/duration-46iwe.md)
  The duration of this `AudioFileResource`.
- [var duration: Duration](audiofileresource/duration-8u518.md)
  The duration of this `AudioFileResource`.
### Type Methods
- [static load(contentsOf:withName:configuration:)](audiofileresource/load(contentsof:withname:configuration:).md)
  Loads an AudioFileResource synchronously.
- [static load(named:from:in:)](audiofileresource/load(named:from:in:).md)
  Loads a preconfigured AudioFileResource from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.
- [static load(named:in:configuration:)](audiofileresource/load(named:in:configuration:).md)
  Loads an AudioFileResource synchronously.

## Relationships

### Inherits From
- [AudioResource](audioresource.md)
### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AudioFileGroupResource](audiofilegroupresource.md)
  An audio file group.
- [class AudioBufferResource](audiobufferresource.md)
  An audio resource that you load from an [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer).
- [struct AudioLibraryComponent](audiolibrarycomponent.md)
  A container for audio resources that you can look up by user-defined names.
- [class AudioResource](audioresource.md)
  A playable audio resource


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource)*