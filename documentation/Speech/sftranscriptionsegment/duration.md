# duration

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The number of seconds it took for the user to speak the utterance represented by the segment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval duration;
```

## Discussion

The [`duration`](./duration.md) contains the number of seconds it took for the user to speak the one or more words (utterance) represented by the segment. For example, the [`SFSpeechRecognizer`](../sfspeechrecognizer.md) sets [`duration`](./duration.md) to `0.6` if the user took `0.6` seconds to say `“time”` in the transcription of `“What time is it?"`.

## See Also

### Getting audio timing information
- [var timestamp: TimeInterval](./timestamp.md)
  The start time of the segment in the processed audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment/duration)*