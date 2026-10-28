# scheduleFile(_:at:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Schedules the playing of an entire audio file.

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
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?, completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?) async
```

```objc
- (void) scheduleFile:(AVAudioFile *) file atTime:(AVAudioTime *) when completionHandler:(AVAudioNodeCompletionHandler) completionHandler;
```

## Discussion

## Parameters

- `file`: The URL of the file to play.
- `when`: The time the buffer plays. For more information, see [Scheduling playback time](../avaudioplayernode.md#Scheduling-playback-time).
- `completionHandler`: The handler the system calls after the player schedules the file for playback on the render thread, or the player stops.

## See Also

### Scheduling files and segments
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulefile%28_,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: (() -> Void)?)](./schedulesegment%28_,startingframe,framecount,at,completionhandler%29.md)
  Schedules the playing of an audio file segment.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulesegment%28_,startingframe,framecount,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [enum AVAudioPlayerNodeCompletionCallbackType](../avaudioplayernodecompletioncallbacktype.md)
  Constants that specify when the framework must invoke the completion handler.
- [typealias AVAudioPlayerNodeCompletionHandler](../avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.
- [typealias AVAudioNodeCompletionHandler](../avaudionodecompletionhandler.md)
  A general callback handler for an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulefile(_:at:completionhandler:))*