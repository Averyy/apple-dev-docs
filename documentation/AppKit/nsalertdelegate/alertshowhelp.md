# alertShowHelp(_:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate when the user clicks the alert’s help button. The delegate causes help to be displayed for an alert, directly or indirectly.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func alertShowHelp(_ alert: NSAlert) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the delegate displayed help directly, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. When [`false`](https://developer.apple.com/documentation/swift/false) and the alert has a help anchor ([`helpAnchor`](nsalert/helpanchor.md)), the application’s help manager displays help using the help anchor.

#### Discussion

The delegate implements this method only to override the help-anchor lookup behavior.

## See Also

- [Sheet Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Sheets.html#//apple_ref/doc/uid/10000002i)
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [Dialogs and Special Panels](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Dialog.html#//apple_ref/doc/uid/10000071i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalertdelegate/alertshowhelp(_:))*