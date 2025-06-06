# AVAudioPlayerNodeCompletionCallbackType.dataRendered

**Framework**: AVFAudio  
**Kind**: case

A completion handler that indicates the player renders the buffer or file data.

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
case dataRendered
```

#### Discussion

This case doesn’t account for any signal processing latencies downstream of the player in the engine.

## See Also

- [AVAudioPlayerNodeCompletionCallbackType.dataConsumed](avaudioplayernodecompletioncallbacktype/dataconsumed.md)
  A completion handler that indicates the player consumes the buffer or file data.
- [AVAudioPlayerNodeCompletionCallbackType.dataPlayedBack](avaudioplayernodecompletioncallbacktype/dataplayedback.md)
  A completion handler that indicates the player finishes the buffer or file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernodecompletioncallbacktype/datarendered)*