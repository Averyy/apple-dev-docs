# NSSpellCheckerDidChangeAutomaticInlinePredictionNotification

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticInlinePredictionMessage`](./nsspellchecker/didchangeautomaticinlinepredictionmessage.md).

**Availability**:
- macOS 14.0+

## Declaration

```c
extern NSNotificationName const NSSpellCheckerDidChangeAutomaticInlinePredictionNotification;
```

## See Also

### Notifications
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](./nsspellchecker/didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellcheckerdidchangeautomaticinlinepredictionnotification)*