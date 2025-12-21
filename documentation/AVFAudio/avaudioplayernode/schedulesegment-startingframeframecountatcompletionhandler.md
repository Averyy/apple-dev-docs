# scheduleSegment(_:startingFrame:frameCount:at:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

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
func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, at when: AVAudioTime?) async
```

#### Discussion

## Parameters

- `file`: The URL of the file to play.
- `startFrame`: The starting frame position in the stream.
- `numberFrames`: The number of frames to play.
- `when`: The time the buffer plays. For more information, see  .
- `completionHandler`: The handler the system calls after the player schedules the segment for playback on the render thread, or the player stops.

## See Also

- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](avaudioplayernode/schedulefile(_:at:completionhandler:).md)
  Schedules the playing of an entire audio file.
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulefile(_:at:completioncallbacktype:completionhandler:).md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completioncallbacktype:completionhandler:).md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completionhandler:).md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:completionhandler:).md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [struct AVAudioPlayerNodeBufferOptions](avaudioplayernodebufferoptions.md)
  The buffer options that control the playback scheduling.
- [enum AVAudioPlayerNodeCompletionCallbackType](avaudioplayernodecompletioncallbacktype.md)
  Constants that specify when the framework must invoke the completion handler.
- [typealias AVAudioPlayerNodeCompletionHandler](avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completionhandler:))*