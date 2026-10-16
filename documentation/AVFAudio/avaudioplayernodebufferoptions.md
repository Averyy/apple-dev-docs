# AVAudioPlayerNodeBufferOptions

**Framework**: AVFAudio  
**Kind**: struct

The buffer options that control the playback scheduling.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVAudioPlayerNodeBufferOptions
```

## Topics

### Creating a buffer option
- [init(rawValue: UInt)](avaudioplayernodebufferoptions/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting standard buffer options
- [static var loops: AVAudioPlayerNodeBufferOptions](avaudioplayernodebufferoptions/loops.md)
  An option that indicates the buffer loops indefinitely.
- [static var interrupts: AVAudioPlayerNodeBufferOptions](avaudioplayernodebufferoptions/interrupts.md)
  An option that indicates the buffer interrupts any buffer in a playing state.
- [static var interruptsAtLoop: AVAudioPlayerNodeBufferOptions](avaudioplayernodebufferoptions/interruptsatloop.md)
  An option that indicates the buffer interrupts any buffer in a playing state at its loop point.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completionhandler:).md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:completionhandler:).md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:attime:options:completioncallbacktype:completionhandler:)-3ewd3.md)
  Schedules playing samples from an audio buffer.
- [func scheduleBuffer(AVReadOnlyAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:attime:options:completioncallbacktype:completionhandler:)-81qje.md)
  Schedules playing samples from a read-only audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernodebufferoptions)*