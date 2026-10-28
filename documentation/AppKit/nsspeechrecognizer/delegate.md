# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the speech recognizer object.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSSpeechRecognizerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSpeechRecognizerDelegate> delegate;
```

## Discussion

The delegate must conform to the [`NSSpeechRecognizerDelegate`](../nsspeechrecognizerdelegate.md) protocol.

## See Also

### Handling the Recognition of a Spoken Command
- [protocol NSSpeechRecognizerDelegate](../nsspeechrecognizerdelegate.md)
  A set of optional methods implemented by delegates of [`NSSpeechRecognizer`](../nsspeechrecognizer.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/delegate)*