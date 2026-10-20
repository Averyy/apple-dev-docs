# AVAudioPlayerNodeCompletionCallbackType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that specify when the framework must invoke the completion handler.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum AVAudioPlayerNodeCompletionCallbackType
```

```c
enum AVAudioPlayerNodeCompletionCallbackType : NSInteger;
```

## Topics

### Creating a callback type
- [init?(rawValue: Int)](./avaudioplayernodecompletioncallbacktype/init%28rawvalue%29.md)
### Choosing a callback type
- [AVAudioPlayerNodeCompletionCallbackType.dataConsumed](./avaudioplayernodecompletioncallbacktype/dataconsumed.md)
  A completion handler that indicates the player consumes the buffer or file data.
- [AVAudioPlayerNodeCompletionCallbackType.dataRendered](./avaudioplayernodecompletioncallbacktype/datarendered.md)
  A completion handler that indicates the player renders the buffer or file data.
- [AVAudioPlayerNodeCompletionCallbackType.dataPlayedBack](./avaudioplayernodecompletioncallbacktype/dataplayedback.md)
  A completion handler that indicates the player finishes the buffer or file data.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scheduling files and segments
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulefile%28_,at,completionhandler%29.md)
  Schedules the playing of an entire audio file.
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulefile%28_,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulesegment%28_,startingframe,framecount,at,completionhandler%29.md)
  Schedules the playing of an audio file segment.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulesegment%28_,startingframe,framecount,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [typealias AVAudioPlayerNodeCompletionHandler](./avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.
- [typealias AVAudioNodeCompletionHandler](./avaudionodecompletionhandler.md)
  A general callback handler for an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernodecompletioncallbacktype)*