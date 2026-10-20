# speechRecognizer(_:didRecognizeCommand:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the recognition engine has recognized the application command `command`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func speechRecognizer(_ sender: NSSpeechRecognizer, didRecognizeCommand command: String)
```

```objc
- (void) speechRecognizer:(NSSpeechRecognizer *) sender didRecognizeCommand:(NSString *) command;
```

#### Discussion

`command` is one of the strings from the array passed to [`commands`](../nsspeechrecognizer/commands.md). The delegate typically evaluates which command was recognized and performs the related action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizerdelegate/speechrecognizer(_:didrecognizecommand:))*