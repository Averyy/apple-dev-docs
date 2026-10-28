# AudioBufferResource

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

An audio resource that you load from an [`AVAudioBuffer`](../AVFAudio/avaudiobuffer.md).

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency class AudioBufferResource
```

## Overview

Use the resource to create an [`AudioPlaybackController`](./audioplaybackcontroller.md) instance by calling an entity’s [`prepareAudio(_:)`](./entity/prepareaudio%28_%29.md) or [`playAudio(_:)`](./entity/playaudio%28_%29.md) function. The controller plays the audio from the location in space of the entity that created the controller.

## Topics

### Creating an audio buffer resource
- [init(buffer: AVAudioBuffer, configuration: AudioBufferResource.Configuration) throws](./audiobufferresource/init%28buffer,configuration%29.md)
  Creates an `AudioBufferResource` with the given `AVAudioBuffer` and configuration.
### Describing the resource
- [let configuration: AudioBufferResource.Configuration](./audiobufferresource/configuration-swift.property.md)
  The configuration for this `AudioBufferResource`.
- [var duration: Duration](./audiobufferresource/duration.md)
  The duration of this `AudioBufferResource`.
### Supporting types
- [AudioBufferResource.Configuration](./audiobufferresource/configuration-swift.struct.md)
### Deprecated
- [init(buffer: AVAudioBuffer, inputMode: AudioResource.InputMode, shouldLoop: Bool) throws](./audiobufferresource/init%28buffer,inputmode,shouldloop%29.md)
  Init an AudioBufferResource from an `AVAudioBuffer` instead of a file location. This is intended for use with `AVSpeechSynthesisVoice`.
- [var shouldLoop: Bool](./audiobufferresource/shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.

## Relationships

### Inherits From
- [AudioResource](./audioresource.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Resource](./resource.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio resources
- [class AudioFileResource](./audiofileresource.md)
  An audio resource that you load from a file or from a URL.
- [class AudioFileGroupResource](./audiofilegroupresource.md)
  An audio file group.
- [struct AudioLibraryComponent](./audiolibrarycomponent.md)
  A container for audio resources that you can look up by user-defined names.
- [class AudioResource](./audioresource.md)
  A playable audio resource
- [AudioResource.Calibration](./audioresource/calibration.md)
  A container for different calibration modes that can be applied for playback.
- [AudioResource.Normalization](./audioresource/normalization.md)
  Normalization adjusts the level of an audio file or buffer to be at a defined target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiobufferresource)*