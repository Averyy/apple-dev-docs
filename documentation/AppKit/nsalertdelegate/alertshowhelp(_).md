# alertShowHelp(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when the user clicks the alert’s help button. The delegate causes help to be displayed for an alert, directly or indirectly.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func alertShowHelp(_ alert: NSAlert) -> Bool
```

```objc
- (BOOL) alertShowHelp:(NSAlert *) alert;
```

## Return Value

[`true`](../../Swift/true.md) when the delegate displayed help directly, [`false`](../../Swift/false.md) otherwise. When [`false`](../../Swift/false.md) and the alert has a help anchor ([`helpAnchor`](../nsalert/helpanchor.md)), the application’s help manager displays help using the help anchor.

## Discussion

The delegate implements this method only to override the help-anchor lookup behavior.

## See Also

### Related Documentation
- [var showsHelp: Bool](../nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [Dialogs and Special Panels](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Dialog.html#//apple_ref/doc/uid/10000071i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalertdelegate/alertshowhelp(_:))*