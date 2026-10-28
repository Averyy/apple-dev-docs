# keyboardSelectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after the selected text input source changes.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class let keyboardSelectionDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextInputContextKeyboardSelectionDidChangeNotification;
```

## Discussion

To observe this notification using Swift concurrency, use [`NSTextInputContext.KeyboardSelectionDidChangeMessage`](./keyboardselectiondidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/keyboardselectiondidchangenotification)*