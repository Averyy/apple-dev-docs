# SFSpeechRecognitionTaskHint

**Framework**: Speech  
**Kind**: enum

The type of task for which you are using speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [class SFSpeechRecognizer](sfspeechrecognizer.md)
  An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.
- [protocol SFSpeechRecognizerDelegate](sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskhint)*