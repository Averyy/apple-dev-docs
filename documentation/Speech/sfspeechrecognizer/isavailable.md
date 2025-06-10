# isAvailable

**Framework**: Speech  
**Kind**: property

A Boolean value that indicates whether the speech recognizer is currently available.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var isAvailable: Bool { get }
```

#### Discussion

When the value of this property is `true`, you may create new speech recognition tasks. When value of this property is `false`, speech recognition services are not available.

## See Also

- [var delegate: (any SFSpeechRecognizerDelegate)?](sfspeechrecognizer/delegate.md)
  The delegate object that handles changes to the availability of speech recognition services.
- [protocol SFSpeechRecognizerDelegate](sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [var supportsOnDeviceRecognition: Bool](sfspeechrecognizer/supportsondevicerecognition.md)
  A Boolean value that indicates whether the speech recognizer can operate without network access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/isavailable)*