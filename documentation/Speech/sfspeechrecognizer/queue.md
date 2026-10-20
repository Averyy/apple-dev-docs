# queue

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The queue on which to execute recognition task handlers and delegate methods.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var queue: OperationQueue { get set }
```

```objc
@property (nonatomic, strong) NSOperationQueue * queue;
```

#### Discussion

The default value of this property is the app’s main queue. Assign a different queue if you want delegate methods and handlers to be executed on a background queue.

The handler you pass to the [`requestAuthorization(_:)`](./requestauthorization%28_%29.md) method does not use this queue.

## See Also

### Configuring the speech recognizer
- [var defaultTaskHint: SFSpeechRecognitionTaskHint](./defaulttaskhint.md)
  A hint that indicates the type of speech recognition being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/queue)*