# runModal()

**Framework**: AppKit  
**Kind**: method

Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal() -> NSApplication.ModalResponse
```

#### Return Value

A response to the alert. See this method’s “Special Considerations” section for details.

#### Discussion

You can create the alert either through the standard allocation and initialization procedure or, if necessary in your app, by using the deprecated compatibility method [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](nsalert/alertwithmessagetext:defaultbutton:alternatebutton:otherbutton:informativetextwithformat:.md).

##### Special Considerations

This method can return values other than those specific to the alert buttons ([`alertFirstButtonReturn`](nsapplication/modalresponse/alertfirstbuttonreturn.md), [`alertSecondButtonReturn`](nsapplication/modalresponse/alertsecondbuttonreturn.md), and so on) if the alert is canceled programatically.

If you use `alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:` to create an alert, the `NSAlertDefaultReturn`, `NSAlertAlternateReturn`, and `NSAlertOtherReturn` constants identify the button used to dismiss the alert. Otherwise, the constants used are the ones described in [`addButton(withTitle:)`](nsalert/addbutton(withtitle:).md).

## See Also

- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nsalert/beginsheetmodal(for:completionhandler:).md)
  Runs the alert modally as a sheet attached to the specified window.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsalert/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the alert modally as an alert sheet attached to a specified window.
- [var suppressionButton: NSButton?](nsalert/suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](nsalert/showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/runmodal())*