# queue

**Framework**: Speech  
**Kind**: property

The queue on which to execute recognition task handlers and delegate methods.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var queue: OperationQueue { get set }
```

#### Discussion

The default value of this property is the app’s main queue. Assign a different queue if you want delegate methods and handlers to be executed on a background queue.

The handler you pass to the [`requestAuthorization(_:)`](sfspeechrecognizer/requestauthorization(_:).md) method does not use this queue.

## See Also

- [var defaultTaskHint: SFSpeechRecognitionTaskHint](sfspeechrecognizer/defaulttaskhint.md)
  A hint that indicates the type of speech recognition being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/queue)*