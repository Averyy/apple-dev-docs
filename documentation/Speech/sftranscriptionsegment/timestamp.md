# timestamp

**Framework**: Speech  
**Kind**: property

The start time of the segment in the processed audio stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

#### Discussion

The [`timestamp`](sftranscriptionsegment/timestamp.md) is the number of seconds between the beginning of the audio content and when the user spoke the word represented by the segment. For example, if the user said the word “time” one second into the transcription “What time is it”, the timestamp would be equal to `1.0`.

## See Also

- [var duration: TimeInterval](sftranscriptionsegment/duration.md)
  The number of seconds it took for the user to speak the utterance represented by the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment/timestamp)*