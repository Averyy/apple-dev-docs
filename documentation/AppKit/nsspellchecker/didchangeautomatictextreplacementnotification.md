# didChangeAutomaticTextReplacementNotification

**Framework**: AppKit  
**Kind**: property

Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didChangeAutomaticTextReplacementNotification: NSNotification.Name
```

#### Discussion

To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextReplacementMessage`](nsspellchecker/didchangeautomatictextreplacementmessage.md).

## See Also

- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomatictextreplacementnotification)*