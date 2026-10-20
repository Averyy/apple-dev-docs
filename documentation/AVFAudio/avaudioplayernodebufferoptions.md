# AVAudioPlayerNodeBufferOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

The buffer options that control the playback scheduling.

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
struct AVAudioPlayerNodeBufferOptions
```

```c
enum AVAudioPlayerNodeBufferOptions : NSUInteger;
```

## Topics

### Creating a buffer option
- [init(rawValue: UInt)](./avaudioplayernodebufferoptions/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard buffer options
- [static var loops: AVAudioPlayerNodeBufferOptions](./avaudioplayernodebufferoptions/loops.md)
  An option that indicates the buffer loops indefinitely.
- [static var interrupts: AVAudioPlayerNodeBufferOptions](./avaudioplayernodebufferoptions/interrupts.md)
  An option that indicates the buffer interrupts any buffer in a playing state.
- [static var interruptsAtLoop: AVAudioPlayerNodeBufferOptions](./avaudioplayernodebufferoptions/interruptsatloop.md)
  An option that indicates the buffer interrupts any buffer in a playing state at its loop point.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Scheduling buffers
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,at,options,completionhandler%29.md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,completionhandler%29.md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulebuffer%28_,at,options,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulebuffer%28_,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-3ewd3.md)
  Schedules playing samples from an audio buffer.
- [func scheduleBuffer(AVReadOnlyAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-81qje.md)
  Schedules playing samples from a read-only audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernodebufferoptions)*