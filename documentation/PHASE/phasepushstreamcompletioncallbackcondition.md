# PHASEPushStreamCompletionCallbackCondition

**Framework**: PHASE  
**Kind**: enum

A status that describes the results after the app schedules a push-stream buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PHASEPushStreamCompletionCallbackCondition
```

#### Overview

A [`PHASEPushStreamNode`](phasepushstreamnode.md) object provides an instance of this class to the completion closure after the app schedules a buffer by calling [`scheduleBuffer(buffer:completionCallbackType:completionHandler:)`](phasepushstreamnode/schedulebuffer(buffer:completioncallbacktype:completionhandler:).md).

## Topics

### Conditions
- [PHASEPushStreamCompletionCallbackCondition.dataRendered](phasepushstreamcompletioncallbackcondition/datarendered.md)
  Indicates the framework invokes the callback when the engine processes the audio for output.
### Initializers
- [init?(rawValue: Int)](phasepushstreamcompletioncallbackcondition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](phasepushstreamnode/schedulebuffer(buffer:).md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](phasepushstreamnode/schedulebuffer(buffer:time:options:).md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](phasepushstreamnode/schedulebuffer(buffer:time:options:completioncallbacktype:completionhandler:).md)
  Schedules audio data playback at a specific time with a completion handler.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](phasepushstreamnode/schedulebuffer(buffer:completioncallbacktype:completionhandler:).md)
  Schedules audio data playback with a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamcompletioncallbackcondition)*