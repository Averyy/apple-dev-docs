# didChangeAutomaticSpellingCorrectionNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSSpellCheckerDidChangeAutomaticSpellingCorrectionNotification;
```

#### Discussion

To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticSpellingCorrectionMessage`](./didchangeautomaticspellingcorrectionmessage.md).

## See Also

### Notifications
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](./didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification)*