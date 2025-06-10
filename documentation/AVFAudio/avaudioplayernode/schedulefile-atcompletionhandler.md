# scheduleFile(_:at:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

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
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?) async
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `file`: The URL of the file to play.
- `when`: The time the buffer plays. For more information, see  .
- `completionHandler`: The handler the system calls after the player schedules the file for playback on the render thread, or the player stops.

## See Also

- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulefile(_:at:completioncallbacktype:completionhandler:).md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: (() -> Void)?)](avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completionhandler:).md)
  Schedules the playing of an audio file segment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulefile(_:at:completionhandler:))*