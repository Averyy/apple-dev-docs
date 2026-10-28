# scheduleSegment(_:startingFrame:frameCount:at:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Schedules the playing of an audio file segment.

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
func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, at when: AVAudioTime?, completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, at when: AVAudioTime?) async
```

```objc
- (void) scheduleSegment:(AVAudioFile *) file startingFrame:(AVAudioFramePosition) startFrame frameCount:(AVAudioFrameCount) numberFrames atTime:(AVAudioTime *) when completionHandler:(AVAudioNodeCompletionHandler) completionHandler;
```

## Discussion

## Parameters

- `file`: The URL of the file to play.
- `startFrame`: The starting frame position in the stream.
- `numberFrames`: The number of frames to play.
- `when`: The time the buffer plays. For more information, see [Scheduling playback time](../avaudioplayernode.md#Scheduling-playback-time).
- `completionHandler`: The handler the system calls after the player schedules the segment for playback on the render thread, or the player stops.

## See Also

### Scheduling files and segments
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](./schedulefile%28_,at,completionhandler%29.md)
  Schedules the playing of an entire audio file.
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulefile%28_,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./schedulesegment%28_,startingframe,framecount,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [enum AVAudioPlayerNodeCompletionCallbackType](../avaudioplayernodecompletioncallbacktype.md)
  Constants that specify when the framework must invoke the completion handler.
- [typealias AVAudioPlayerNodeCompletionHandler](../avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.
- [typealias AVAudioNodeCompletionHandler](../avaudionodecompletionhandler.md)
  A general callback handler for an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completionhandler:))*