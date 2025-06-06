# PHASEPushStreamNode

**Framework**: PHASE  
**Kind**: class

An audio stream you manage to provide a sound buffer data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEPushStreamNode
```

#### Overview

A sound event’s [`pushStreamNodes`](phasesoundevent/pushstreamnodes.md) dictionary populates with an instance of this class when PHASE invokes a  [`PHASEPushStreamNodeDefinition`](phasepushstreamnodedefinition.md) in your event node tree.

Your app provides the audio data that the sound event plays by calling one or more of this class’s buffer-scheduling functions, for example, [`scheduleBuffer(buffer:)`](phasepushstreamnode/schedulebuffer(buffer:).md).

## Topics

### Inspecting Stream Properties
- [var mixer: PHASEMixer](phasepushstreamnode/mixer.md)
  The audio stream’s output pipeline.
- [var format: AVAudioFormat](phasepushstreamnode/format.md)
  The format of the audio stream data.
### Providing Audio Data
- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](phasepushstreamnode/schedulebuffer(buffer:).md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](phasepushstreamnode/schedulebuffer(buffer:time:options:).md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](phasepushstreamnode/schedulebuffer(buffer:time:options:completioncallbacktype:completionhandler:).md)
  Schedules audio data playback at a specific time with a completion handler.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](phasepushstreamnode/schedulebuffer(buffer:completioncallbacktype:completionhandler:).md)
  Schedules audio data playback with a completion handler.
- [enum PHASEPushStreamCompletionCallbackCondition](phasepushstreamcompletioncallbackcondition.md)
  A status that describes the results after the app schedules a push-stream buffer.
### Controlling Playback
- [var gainMetaParameter: PHASENumberMetaParameter?](phasepushstreamnode/gainmetaparameter.md)
  A meta parameter for dynamic loudness control.
- [var rateMetaParameter: PHASENumberMetaParameter?](phasepushstreamnode/ratemetaparameter.md)
  A meta parameter for dynamic rate control.

## Relationships

### Inherits From
- [PHASEStreamNode](phasestreamnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASESamplerNodeDefinition](phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [struct PHASEPushStreamBufferOptions](phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [enum PHASECalibrationMode](phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode)*