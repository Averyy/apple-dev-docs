# AVAudioPlayerNodeCompletionCallbackType.dataPlayedBack

**Framework**: AVFAudio  
**Kind**: case

A completion handler that indicates the player finishes the buffer or file data.

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
case dataPlayedBack
```

#### Discussion

The completion handler is applicable when the engine is rendering to or from an audio device.

It accounts for both signal processing latencies downstream of the player in the engine, and (possibly significant) latency in the audio playback device.

## See Also

- [AVAudioPlayerNodeCompletionCallbackType.dataConsumed](avaudioplayernodecompletioncallbacktype/dataconsumed.md)
  A completion handler that indicates the player consumes the buffer or file data.
- [AVAudioPlayerNodeCompletionCallbackType.dataRendered](avaudioplayernodecompletioncallbacktype/datarendered.md)
  A completion handler that indicates the player renders the buffer or file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernodecompletioncallbacktype/dataplayedback)*