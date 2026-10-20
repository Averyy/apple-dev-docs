# scheduleBuffer(buffer:time:options:completionCallbackType:completionHandler:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Schedules audio data playback at a specific time with a completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func scheduleBuffer(buffer: AVAudioPCMBuffer, time when: AVAudioTime?, options: PHASEPushStreamBufferOptions = [], completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: @escaping @Sendable (PHASEPushStreamCompletionCallbackCondition) -> Void)
```

```swift
func scheduleBuffer(buffer: AVAudioPCMBuffer, time when: AVAudioTime?, options: PHASEPushStreamBufferOptions = [], completionCallbackType: PHASEPushStreamCompletionCallbackCondition) async -> PHASEPushStreamCompletionCallbackCondition
```

```objc
- (void) scheduleBuffer:(AVAudioPCMBuffer *) buffer atTime:(AVAudioTime *) when options:(PHASEPushStreamBufferOptions) options completionCallbackType:(PHASEPushStreamCompletionCallbackCondition) completionCallbackType completionHandler:(void (^)(PHASEPushStreamCompletionCallbackCondition callbackType)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func scheduleBuffer(buffer: AVAudioPCMBuffer, time when: AVAudioTime?, options: PHASEPushStreamBufferOptions = [], completionCallbackType: PHASEPushStreamCompletionCallbackCondition) async -> PHASEPushStreamCompletionCallbackCondition
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `buffer`: Data that represents one portion of a contiguous audio stream.
- `when`: The time to play the buffer.
- `options`: The options for looping and buffer interruption.
- `completionCallbackType`: The specific event on which to handle completion.
- `completionHandler`: Code the framework runs on completion or when the player stops.

## See Also

### Providing Audio Data
- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](./schedulebuffer%28buffer%29.md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](./schedulebuffer%28buffer,time,options%29.md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](./schedulebuffer%28buffer,completioncallbacktype,completionhandler%29.md)
  Schedules audio data playback with a completion handler.
- [enum PHASEPushStreamCompletionCallbackCondition](../phasepushstreamcompletioncallbackcondition.md)
  A status that describes the results after the app schedules a push-stream buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/schedulebuffer(buffer:time:options:completioncallbacktype:completionhandler:))*