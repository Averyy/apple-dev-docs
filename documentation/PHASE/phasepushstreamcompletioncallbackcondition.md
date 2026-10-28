# PHASEPushStreamCompletionCallbackCondition

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

A status that describes the results after the app schedules a push-stream buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum PHASEPushStreamCompletionCallbackCondition
```

```c
enum PHASEPushStreamCompletionCallbackCondition : NSInteger;
```

## Overview

A [`PHASEPushStreamNode`](./phasepushstreamnode.md) object provides an instance of this class to the completion closure after the app schedules a buffer by calling [`scheduleBuffer(buffer:completionCallbackType:completionHandler:)`](./phasepushstreamnode/schedulebuffer%28buffer,completioncallbacktype,completionhandler%29.md).

## Topics

### Conditions
- [PHASEPushStreamCompletionCallbackCondition.dataRendered](./phasepushstreamcompletioncallbackcondition/datarendered.md)
  Indicates the framework invokes the callback when the engine processes the audio for output.
### Initializers
- [init?(rawValue: Int)](./phasepushstreamcompletioncallbackcondition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing Audio Data
- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](./phasepushstreamnode/schedulebuffer%28buffer%29.md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](./phasepushstreamnode/schedulebuffer%28buffer,time,options%29.md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./phasepushstreamnode/schedulebuffer%28buffer,time,options,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback at a specific time with a completion handler.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./phasepushstreamnode/schedulebuffer%28buffer,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback with a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamcompletioncallbackcondition)*