# AudioGeneratorController

**Framework**: RealityKit  
**Kind**: class

A controller that manages the playback of a real-time audio stream.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
class AudioGeneratorController
```

#### Overview

To receive an audio generator controller, call an entity’s [`prepareAudio(configuration:_:)`](entity/prepareaudio(configuration:_:).md) or [`playAudio(configuration:_:)`](entity/playaudio(configuration:_:).md) method.

The following examples show how you can use the controller:

```objc
/// myHandler.mm
AVAudioSourceNodeRenderBlock myHandler = ^OSStatus(BOOL *isSilence,
                                                   const AudioTimeStamp *timestamp,
                                                   AVAudioFrameCount frameCount,
                                                   AudioBufferList *outputData) {

   double phase = FREQUENCY * timestamp->mSampleTime * (1.f / SAMPLE_RATE);
   for (int idx = 0; idx < frameCount; idx++) {
       ((Float32 *)outputData->mBuffers[0].mData)[idx] = sin(phase * 2.f * M_PI) * 0.5;
       phase += (FREQUENCY / SAMPLE_RATE);
   }

   return 0;
};
```

```swift
// Create a configuration.
var config = AudioGeneratorConfiguration(kAudioChannelLayoutTag_Mono)

// Prepare a closure that you define in myHandler.mm.
var controller = myEntity.prepareAudio(configuration: config, myHandler)

controller.gain = -3.0
controller.play()
```

During playback, the audio appears to come from the entity that you use to create the controller. As a person moves around the MR scene, RealityKit modulates the characteristics of the audio to account for their location.

> **Note**: Audio stops rendering when the system deallocates `AudioGeneratorController`. Create another `AudioGeneratorController` to restart audio.

Call [`stop()`](audiogeneratorcontroller/stop().md) to halt the audio, and [`play()`](audiogeneratorcontroller/play().md) to restart the stream.

## Topics

### Instance Properties
- [let configuration: AudioGeneratorConfiguration](audiogeneratorcontroller/configuration.md)
  The configuration with rendering parameters for the render handler.
- [var entity: Entity?](audiogeneratorcontroller/entity.md)
  The entity the audio stream emanates from.
- [var gain: Audio.Decibel](audiogeneratorcontroller/gain.md)
  The gain in decibels of the audio generator controller output.
- [var isPlaying: Bool](audiogeneratorcontroller/isplaying.md)
  A Boolean value that indicates whether playback is currently active.
### Instance Methods
- [func play()](audiogeneratorcontroller/play.md)
  Begins the audio stream from the generator render handler.
- [func stop()](audiogeneratorcontroller/stop.md)
  Stops playback of the render handler.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AudioPlaybackController](audioplaybackcontroller.md)
  A controller that manages an audio playback instance.
- [struct AudioGeneratorConfiguration](audiogeneratorconfiguration.md)
  A container for various settings for preparing and playing an AudioGeneratorController.
- [enum AudioEvents](audioevents.md)
  Events associated with audio playback.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiogeneratorcontroller)*