# SFSpeechRecognitionTaskHint

**Framework**: Speech  
**Kind**: enum

The type of task for which you are using speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum SFSpeechRecognitionTaskHint
```

## Topics

### Hints
- [SFSpeechRecognitionTaskHint.unspecified](sfspeechrecognitiontaskhint/unspecified.md)
  An unspecified type of task.
- [SFSpeechRecognitionTaskHint.dictation](sfspeechrecognitiontaskhint/dictation.md)
  A task that uses captured speech for text entry.
- [SFSpeechRecognitionTaskHint.search](sfspeechrecognitiontaskhint/search.md)
  A task that uses captured speech to specify search terms.
- [SFSpeechRecognitionTaskHint.confirmation](sfspeechrecognitiontaskhint/confirmation.md)
  A task that uses captured speech for short, confirmation-style requests.
### Initializers
- [init?(rawValue: Int)](sfspeechrecognitiontaskhint/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var taskHint: SFSpeechRecognitionTaskHint](sfspeechrecognitionrequest/taskhint.md)
  A value that indicates the type of speech recognition being performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint)*