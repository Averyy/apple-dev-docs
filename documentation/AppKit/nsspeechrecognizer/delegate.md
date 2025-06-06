# delegate

**Framework**: AppKit  
**Kind**: property

The delegate for the speech recognizer object.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSSpeechRecognizerDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NSSpeechRecognizerDelegate`](nsspeechrecognizerdelegate.md) protocol.

## See Also

- [protocol NSSpeechRecognizerDelegate](nsspeechrecognizerdelegate.md)
  A set of optional methods implemented by delegates of [`NSSpeechRecognizer`](nsspeechrecognizer.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/delegate)*