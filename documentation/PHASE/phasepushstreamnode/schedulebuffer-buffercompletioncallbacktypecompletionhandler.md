# scheduleBuffer(buffer:completionCallbackType:completionHandler:)

**Framework**: PHASE  
**Kind**: method

Schedules audio data playback with a completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition) async -> PHASEPushStreamCompletionCallbackCondition
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func scheduleBuffer(buffer: AVAudioPCMBuffer, completionCallbackType: PHASEPushStreamCompletionCallbackCondition) async -> PHASEPushStreamCompletionCallbackCondition
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `buffer`: Data that represents one portion of a contiguous audio stream.
- `completionCallbackType`: The specific event on which to handle completion.
- `completionHandler`: Code the framework runs on completion or when the player stops.

## See Also

- [func scheduleBuffer(buffer: AVAudioPCMBuffer)](phasepushstreamnode/schedulebuffer(buffer:).md)
  Schedules audio data for playback.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions)](phasepushstreamnode/schedulebuffer(buffer:time:options:).md)
  Schedules audio data playback at a specific time.
- [func scheduleBuffer(buffer: AVAudioPCMBuffer, time: AVAudioTime?, options: PHASEPushStreamBufferOptions, completionCallbackType: PHASEPushStreamCompletionCallbackCondition, completionHandler: (PHASEPushStreamCompletionCallbackCondition) -> Void)](phasepushstreamnode/schedulebuffer(buffer:time:options:completioncallbacktype:completionhandler:).md)
  Schedules audio data playback at a specific time with a completion handler.
- [enum PHASEPushStreamCompletionCallbackCondition](phasepushstreamcompletioncallbackcondition.md)
  A status that describes the results after the app schedules a push-stream buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/schedulebuffer(buffer:completioncallbacktype:completionhandler:))*