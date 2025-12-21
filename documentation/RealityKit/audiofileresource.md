# AudioFileResource

**Framework**: RealityKit  
**Kind**: class

An audio resource that you load from a file or from a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
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
- [convenience init(named: String, from: String, in: Bundle?) async throws](audiofileresource/init(named:from:in:).md)
  Initializes a preconfigured AudioFileResource asynchronously from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.
- [convenience init(named: String, in: Bundle?, configuration: AudioFileResource.Configuration) async throws](audiofileresource/init(named:in:configuration:).md)
  Initializes an AudioFileResource asynchronously.
### Loading audio from a URL
- [convenience init(contentsOf: URL, withName: String?, configuration: AudioFileResource.Configuration) async throws](audiofileresource/init(contentsof:withname:configuration:).md)
  Initializes an AudioFileResource asynchronously.
### Describing the resource
- [let configuration: AudioFileResource.Configuration](audiofileresource/configuration-swift.property.md)
  The configuration of this `AudioFileResource`.
- [var duration: Duration](audiofileresource/duration.md)
  The duration of this `AudioFileResource`.
- [let name: String](audiofileresource/name.md)
  The name of this `AudioFileResource`.
### Supporting types
- [AudioFileResource.Configuration](audiofileresource/configuration-swift.struct.md)
  A container for various settings for loading an audio file resource.
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
### Operators
- [static func == (AudioFileResource, AudioFileResource) -> Bool](audiofileresource/==(_:_:).md)
### Type Methods
- [static func load(contentsOf: URL, withName: String?, configuration: AudioFileResource.Configuration) throws -> AudioFileResource](audiofileresource/load(contentsof:withname:configuration:).md)
  Loads an AudioFileResource synchronously.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileResource](audiofileresource/load(named:from:in:).md)
  Loads a preconfigured AudioFileResource from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.
- [static func load(named: String, in: Bundle?, configuration: AudioFileResource.Configuration) throws -> AudioFileResource](audiofileresource/load(named:in:configuration:).md)
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
- [AudioResource.Calibration](audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource)*