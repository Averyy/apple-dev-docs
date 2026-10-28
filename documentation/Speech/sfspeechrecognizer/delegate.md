# delegate

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The delegate object that handles changes to the availability of speech recognition services.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any SFSpeechRecognizerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<SFSpeechRecognizerDelegate> delegate;
```

## Discussion

Provide a delegate object when you want to monitor changes to the availability of speech recognition services. Your delegate object must conform to the [`SFSpeechRecognizerDelegate`](../sfspeechrecognizerdelegate.md) protocol.

## See Also

### Monitoring speech recognition availability
- [protocol SFSpeechRecognizerDelegate](../sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether the speech recognizer is currently available.
- [var supportsOnDeviceRecognition: Bool](./supportsondevicerecognition.md)
  A Boolean value that indicates whether the speech recognizer can operate without network access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/delegate)*