# AVAudioSession.IOType.aggregated

**Framework**: AVFAudio  
**Kind**: case

An I/O type that indicates if audio input and output should be presented in the same realtime I/O callback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case aggregated
```

#### Discussion

Use this value if your session uses [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and requires input and output audio to be presented in the same realtime I/O callback. For example, if your app uses a Remote I/O with both input and output enabled.

An audio session’s preference to use aggregated I/O won’t be honored if it specifies the [`mixWithOthers`](avaudiosession/categoryoptions-swift.struct/mixwithothers.md) option and another app’s audio session was already active with nonmixable, nonaggregated I/O.

## See Also

- [AVAudioSession.IOType.notSpecified](avaudiosession/iotype/notspecified.md)
  The default audio session I/O type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iotype/aggregated)*