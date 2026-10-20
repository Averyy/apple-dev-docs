# AVAudioSession.IOType.aggregated

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

An I/O type that indicates if audio input and output should be presented in the same realtime I/O callback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case aggregated
```

```c
AVAudioSessionIOTypeAggregated
```

#### Discussion

Use this value if your session uses [`playAndRecord`](../category-swift.struct/playandrecord.md) and requires input and output audio to be presented in the same realtime I/O callback. For example, if your app uses a Remote I/O with both input and output enabled.

An audio session’s preference to use aggregated I/O won’t be honored if it specifies the [`mixWithOthers`](../categoryoptions-swift.struct/mixwithothers.md) option and another app’s audio session was already active with nonmixable, nonaggregated I/O.

## See Also

### Choosing an I/O type
- [AVAudioSession.IOType.notSpecified](./notspecified.md)
  The default audio session I/O type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iotype/aggregated)*