# scheduleBuffer(_:at:options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Schedules the playing samples from an audio buffer at the time and playback options you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions = [], completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions = []) async
```

```objc
- (void) scheduleBuffer:(AVAudioPCMBuffer *) buffer atTime:(AVAudioTime *) when options:(AVAudioPlayerNodeBufferOptions) options completionHandler:(AVAudioNodeCompletionHandler) completionHandler;
```

## Discussion

## Parameters

- `buffer`: The buffer to play.
- `when`: The time the buffer plays. For more information, see [Scheduling playback time](../avaudioplayernode.md#Scheduling-playback-time).
- `options`: The playback options that control buffer scheduling.
- `completionHandler`: The handler the system calls after the player schedules the buffer for playback on the render thread, or the player stops.

## See Also

### Scheduling buffers
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](./schedulebuffer%28_,completionhandler%29.md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulebuffer%28_,at,options,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulebuffer%28_,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-3ewd3.md)
  Schedules playing samples from an audio buffer.
- [func scheduleBuffer(AVReadOnlyAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-81qje.md)
  Schedules playing samples from a read-only audio buffer.
- [struct AVAudioPlayerNodeBufferOptions](../avaudioplayernodebufferoptions.md)
  The buffer options that control the playback scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulebuffer(_:at:options:completionhandler:))*