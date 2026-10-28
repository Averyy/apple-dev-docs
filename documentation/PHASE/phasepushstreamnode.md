# PHASEPushStreamNode

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

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

```objc
@interface PHASEPushStreamNode : PHASEStreamNode
```

## Overview

A sound event’s [`pushStreamNodes`](./phasesoundevent/pushstreamnodes.md) dictionary populates with an instance of this class when PHASE invokes a  [`PHASEPushStreamNodeDefinition`](./phasepushstreamnodedefinition.md) in your event node tree.

Your app provides the audio data that the sound event plays by calling one or more of this class’s buffer-scheduling functions, for example, [`scheduleBuffer(buffer:)`](./phasepushstreamnode/schedulebuffer%28buffer%29.md).

## Topics

### Inspecting Stream Properties
- [var mixer: PHASEMixer](./phasepushstreamnode/mixer.md)
  The audio stream’s output pipeline.
- [var format: AVAudioFormat](./phasepushstreamnode/format.md)
  The format of the audio stream data.
### Providing Audio Data
- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](./phasepushstreamnode/schedulebuffer%28buffer%29.md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](./phasepushstreamnode/schedulebuffer%28buffer,time,options%29.md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./phasepushstreamnode/schedulebuffer%28buffer,time,options,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback at a specific time with a completion handler.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./phasepushstreamnode/schedulebuffer%28buffer,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback with a completion handler.
- [enum PHASEPushStreamCompletionCallbackCondition](./phasepushstreamcompletioncallbackcondition.md)
  A status that describes the results after the app schedules a push-stream buffer.
### Controlling Playback
- [var gainMetaParameter: PHASENumberMetaParameter?](./phasepushstreamnode/gainmetaparameter.md)
  A meta parameter for dynamic loudness control.
- [var rateMetaParameter: PHASENumberMetaParameter?](./phasepushstreamnode/ratemetaparameter.md)
  A meta parameter for dynamic rate control.

## Relationships

### Inherits From
- [PHASEStreamNode](./phasestreamnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Audio-Providing Nodes
- [class PHASESamplerNodeDefinition](./phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](./phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](./phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [struct PHASEPushStreamBufferOptions](./phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [enum PHASECalibrationMode](./phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](./phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode)*