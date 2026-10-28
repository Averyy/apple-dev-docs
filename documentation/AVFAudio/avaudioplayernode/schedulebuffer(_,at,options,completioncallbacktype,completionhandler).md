# scheduleBuffer(_:at:options:completionCallbackType:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Schedules the playing samples from an audio buffer with the playback options you specify.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions = [], completionCallbackType callbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (@Sendable (AVAudioPlayerNodeCompletionCallbackType) -> Void)? = nil)
```

```swift
func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions = [], completionCallbackType callbackType: AVAudioPlayerNodeCompletionCallbackType) async -> AVAudioPlayerNodeCompletionCallbackType
```

```objc
- (void) scheduleBuffer:(AVAudioPCMBuffer *) buffer atTime:(AVAudioTime *) when options:(AVAudioPlayerNodeBufferOptions) options completionCallbackType:(AVAudioPlayerNodeCompletionCallbackType) callbackType completionHandler:(AVAudioPlayerNodeCompletionHandler) completionHandler;
```

## Discussion

## Parameters

- `buffer`: The buffer to play.
- `when`: The time the buffer plays.
- `options`: The playback options that control buffer scheduling.
- `callbackType`: The option to specify when the system must call the completion handler.
- `completionHandler`: The handler the system calls after the player schedules the buffer for playback on the render thread, or the player stops.

## See Also

### Scheduling buffers
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](./schedulebuffer%28_,at,options,completionhandler%29.md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](./schedulebuffer%28_,completionhandler%29.md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulebuffer%28_,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-3ewd3.md)
  Schedules playing samples from an audio buffer.
- [func scheduleBuffer(AVReadOnlyAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-81qje.md)
  Schedules playing samples from a read-only audio buffer.
- [struct AVAudioPlayerNodeBufferOptions](../avaudioplayernodebufferoptions.md)
  The buffer options that control the playback scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulebuffer(_:at:options:completioncallbacktype:completionhandler:))*