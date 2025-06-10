# AVAudioNodeTapBlock

**Framework**: AVFAudio  
**Kind**: typealias

The block that receives copies of the output of an audio node.

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
typealias AVAudioNodeTapBlock = (AVAudioPCMBuffer, AVAudioTime) -> Void
```

#### Discussion

> ❗ **Important**:  The framework may invoke this callback on a thread other than the main thread.

## Parameters

- `buffer`: A buffer of audio the system captures from the output of an audio node
- `when`: The time the system captures the buffer.

## See Also

- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](avaudionode/installtap(onbus:buffersize:format:block:).md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [func removeTap(onBus: AVAudioNodeBus)](avaudionode/removetap(onbus:).md)
  Removes an audio tap on a bus you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionodetapblock)*