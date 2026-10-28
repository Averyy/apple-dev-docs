# scheduleBuffer(buffer:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Schedules audio data for playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func scheduleBuffer(buffer: AVAudioPCMBuffer)
```

```objc
- (void) scheduleBuffer:(AVAudioPCMBuffer *) buffer;
```

## Discussion

The framework processes this buffer after completing previously scheduled buffers. The buffer’s data format needs to match [`format`](./format.md).

## Parameters

- `buffer`: Data that represents one portion of a contiguous audio stream.

## See Also

### Providing Audio Data
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](./schedulebuffer%28buffer,time,options%29.md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./schedulebuffer%28buffer,time,options,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback at a specific time with a completion handler.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./schedulebuffer%28buffer,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback with a completion handler.
- [enum PHASEPushStreamCompletionCallbackCondition](../phasepushstreamcompletioncallbackcondition.md)
  A status that describes the results after the app schedules a push-stream buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/schedulebuffer(buffer:))*