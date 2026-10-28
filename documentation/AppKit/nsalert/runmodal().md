# runModal()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.

**Availability**:
- macOS

## Declaration

```swift
func runModal() -> NSApplication.ModalResponse
```

```objc
- (NSModalResponse) runModal;
```

## Return Value

A response to the alert. See this method’s “Special Considerations” section for details.

## Discussion

You can create the alert either through the standard allocation and initialization procedure or, if necessary in your app, by using the deprecated compatibility method [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](./alertwithmessagetext_defaultbutton_alternatebutton_otherbutton_informativetextwithformat_.md).

### Special Considerations

This method can return values other than those specific to the alert buttons ([`alertFirstButtonReturn`](../nsapplication/modalresponse/alertfirstbuttonreturn.md), [`alertSecondButtonReturn`](../nsapplication/modalresponse/alertsecondbuttonreturn.md), and so on) if the alert is canceled programatically.

If you use `alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:` to create an alert, the `NSAlertDefaultReturn`, `NSAlertAlternateReturn`, and `NSAlertOtherReturn` constants identify the button used to dismiss the alert. Otherwise, the constants used are the ones described in [`addButton(withTitle:)`](./addbutton%28withtitle%29.md).

## See Also

### Displaying alerts
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./beginsheetmodal%28for,completionhandler%29.md)
  Runs the alert modally as a sheet attached to the specified window.
- [var suppressionButton: NSButton?](./suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](./showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the alert modally as an alert sheet attached to a specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/runmodal())*