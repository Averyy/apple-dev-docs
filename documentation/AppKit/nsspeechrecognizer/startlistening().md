# startListening()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the speech recognition engine to begin listening for commands.

**Availability**:
- macOS

## Declaration

```swift
func startListening()
```

```objc
- (void) startListening;
```

## Discussion

When a command is recognized the message [`speechRecognizer(_:didRecognizeCommand:)`](../nsspeechrecognizerdelegate/speechrecognizer%28_,didrecognizecommand%29.md) is sent to the delegate.

## See Also

### Listening
- [func stopListening()](./stoplistening%28%29.md)
  Tells the speech recognition engine to suspend listening for commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/startlistening())*