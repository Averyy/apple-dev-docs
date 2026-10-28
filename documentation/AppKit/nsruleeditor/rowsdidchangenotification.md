# rowsDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

This notification is posted to the default notification center whenever the view’s rows change.

**Availability**:
- macOS

## Declaration

```swift
class let rowsDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSRuleEditorRowsDidChangeNotification;
```

## Discussion

The object is the rule editor; there is no `userInfo` object.

To observe this notification using Swift concurrency, use [`NSRuleEditor.RowsDidChangeMessage`](./rowsdidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowsdidchangenotification)*