# startListening()

**Framework**: AppKit  
**Kind**: method

Tells the speech recognition engine to begin listening for commands.

**Availability**:
- macOS ?+

## Declaration

```swift
func startListening()
```

#### Discussion

When a command is recognized the message [`speechRecognizer(_:didRecognizeCommand:)`](nsspeechrecognizerdelegate/speechrecognizer(_:didrecognizecommand:).md) is sent to the delegate.

## See Also

- [func stopListening()](nsspeechrecognizer/stoplistening.md)
  Tells the speech recognition engine to suspend listening for commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/startlistening())*