# supportsOnDeviceRecognition

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the speech recognizer can operate without network access.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var supportsOnDeviceRecognition: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsOnDeviceRecognition;
```

#### Discussion

An [`SFSpeechRecognitionRequest`](../sfspeechrecognitionrequest.md) can only honor its [`requiresOnDeviceRecognition`](../sfspeechrecognitionrequest/requiresondevicerecognition.md) property if [`supportsOnDeviceRecognition`](./supportsondevicerecognition.md) is `true`. If [`supportsOnDeviceRecognition`](./supportsondevicerecognition.md) is `false`, the [`SFSpeechRecognizer`](../sfspeechrecognizer.md) requires a network in order to recognize speech.

## See Also

### Monitoring speech recognition availability
- [var delegate: (any SFSpeechRecognizerDelegate)?](./delegate.md)
  The delegate object that handles changes to the availability of speech recognition services.
- [protocol SFSpeechRecognizerDelegate](../sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the speech recognizer is currently available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/supportsondevicerecognition)*