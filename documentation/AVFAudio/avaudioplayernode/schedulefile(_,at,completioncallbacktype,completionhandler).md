# scheduleFile(_:at:completionCallbackType:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Schedules the playing of an entire audio file with a callback option you specify.

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
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?, completionCallbackType callbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (@Sendable (AVAudioPlayerNodeCompletionCallbackType) -> Void)? = nil)
```

```swift
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?, completionCallbackType callbackType: AVAudioPlayerNodeCompletionCallbackType) async -> AVAudioPlayerNodeCompletionCallbackType
```

```objc
- (void) scheduleFile:(AVAudioFile *) file atTime:(AVAudioTime *) when completionCallbackType:(AVAudioPlayerNodeCompletionCallbackType) callbackType completionHandler:(AVAudioPlayerNodeCompletionHandler) completionHandler;
```

#### Discussion

## Parameters

- `file`: The file to play.
- `when`: The time the file plays.
- `callbackType`: The option to specify when the system must call the completion handler.
- `completionHandler`: The handler the system calls after the player schedules the file for playback on the render thread, or the player stops.

## See Also

### Scheduling files and segments
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](./schedulefile%28_,at,completionhandler%29.md)
  Schedules the playing of an entire audio file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulefile(_:at:completioncallbacktype:completionhandler:))*