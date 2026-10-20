# taskHint

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

A value that indicates the type of speech recognition being performed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var taskHint: SFSpeechRecognitionTaskHint { get set }
```

```objc
@property (nonatomic) SFSpeechRecognitionTaskHint taskHint;
```

#### Discussion

The default value of this property is [`SFSpeechRecognitionTaskHint.unspecified`](../sfspeechrecognitiontaskhint/unspecified.md). For a valid list of values, see [`SFSpeechRecognitionTaskHint`](../sfspeechrecognitiontaskhint.md).

## See Also

### Speech Type Classification
- [enum SFSpeechRecognitionTaskHint](../sfspeechrecognitiontaskhint.md)
  The type of task for which you are using speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/taskhint)*