# didChangeAutomaticTextReplacementNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didChangeAutomaticTextReplacementNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSSpellCheckerDidChangeAutomaticTextReplacementNotification;
```

#### Discussion

To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextReplacementMessage`](./didchangeautomatictextreplacementmessage.md).

## See Also

### Notifications
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](./didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [NSSpellCheckerDidChangeAutomaticInlinePredictionNotification](../nsspellcheckerdidchangeautomaticinlinepredictionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticInlinePredictionMessage`](./didchangeautomaticinlinepredictionmessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomatictextreplacementnotification)*