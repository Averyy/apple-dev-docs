# NSSpeechRecognizerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSSpeechRecognizer`](./nsspeechrecognizer.md) objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSSpeechRecognizerDelegate : NSObjectProtocol
```

```objc
@protocol NSSpeechRecognizerDelegate <NSObject>
```

## Topics

### Recognizing Commands
- [func speechRecognizer(NSSpeechRecognizer, didRecognizeCommand: String)](./nsspeechrecognizerdelegate/speechrecognizer%28_,didrecognizecommand%29.md)
  Invoked when the recognition engine has recognized the application command `command`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling the Recognition of a Spoken Command
- [var delegate: (any NSSpeechRecognizerDelegate)?](./nsspeechrecognizer/delegate.md)
  The delegate for the speech recognizer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizerdelegate)*