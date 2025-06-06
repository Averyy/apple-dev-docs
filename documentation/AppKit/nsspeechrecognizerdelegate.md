# NSSpeechRecognizerDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of [`NSSpeechRecognizer`](nsspeechrecognizer.md) objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSpeechRecognizerDelegate : NSObjectProtocol
```

## Topics

### Recognizing Commands
- [func speechRecognizer(NSSpeechRecognizer, didRecognizeCommand: String)](nsspeechrecognizerdelegate/speechrecognizer(_:didrecognizecommand:).md)
  Invoked when the recognition engine has recognized the application command `command`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSSpeechRecognizerDelegate)?](nsspeechrecognizer/delegate.md)
  The delegate for the speech recognizer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizerdelegate)*