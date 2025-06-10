# defaultTaskHint

**Framework**: Speech  
**Kind**: property

A hint that indicates the type of speech recognition being requested.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var defaultTaskHint: SFSpeechRecognitionTaskHint { get set }
```

#### Discussion

By default, the value of this property overrides the [`SFSpeechRecognitionTaskHint.unspecified`](sfspeechrecognitiontaskhint/unspecified.md) value for requests. For possible values, see [`SFSpeechRecognitionTaskHint`](sfspeechrecognitiontaskhint.md).

## See Also

- [var queue: OperationQueue](sfspeechrecognizer/queue.md)
  The queue on which to execute recognition task handlers and delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/defaulttaskhint)*