# ruleEditorRowsDidChange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver that a rule editor’s rows changed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func ruleEditorRowsDidChange(_ notification: Notification)
```

```objc
- (void) ruleEditorRowsDidChange:(NSNotification *) notification;
```

## Discussion

If the delegate implements this method, [`NSRuleEditor`](../nsruleeditor.md) automatically registers its delegate to receive [`rowsDidChangeNotification`](../nsruleeditor/rowsdidchangenotification.md) notifications.

## Parameters

- `notification`: A notification named[`rowsDidChangeNotification`](../nsruleeditor/rowsdidchangenotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditorrowsdidchange(_:))*