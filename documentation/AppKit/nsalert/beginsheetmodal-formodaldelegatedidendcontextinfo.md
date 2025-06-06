# beginSheetModal(for:modalDelegate:didEnd:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Runs the alert modally as an alert sheet attached to a specified window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheetModal(for window: NSWindow, modalDelegate delegate: Any?, didEnd didEndSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

You can create the required `NSAlert` object either through the standard allocate-initialize procedure or by using the compatibility method [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](nsalert/alertwithmessagetext:defaultbutton:alternatebutton:otherbutton:informativetextwithformat:.md).

The `alertDidEndSelector` argument must be a selector that takes three arguments, and the corresponding method should have a declaration modeled on the following example:

```objc
- (void) alertDidEnd:(NSAlert *)alert returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo;
```

where `alert` is the `NSAlert` object, `returnCode` specifies which button the user clicked, and `contextInfo` is the same `contextInfo` passed in the original message. The `returnCode` argument identifies which button was used to dismiss the alert (see this method’s “Special Considerations” section). The modal delegate determines which button was clicked (“OK”, “Cancel”, and so on) and proceeds accordingly.

If you want to dismiss the sheet from within the `alertDidEndSelector` method before the modal delegate carries out an action in response to the return value, send [`orderOut(_:)`](nswindow/orderout(_:).md) ([`NSWindow`](nswindow.md)) to the window object obtained by sending [`window`](nsalert/window.md) to the `alert` argument. This allows you to chain sheets, for example, by dismissing one sheet before showing the next from within the `alertDidEndSelector` method. Note that you should be careful not to call [`orderOut(_:)`](nswindow/orderout(_:).md) on the sheet from elsewhere in your program before the `alertDidEndSelector` method is invoked because the parent window can hang when another alert is requested. If you need to do this, use the `NSApplication` method [`endSheet(_:)`](nsapplication/endsheet(_:).md).

##### Special Considerations

If you use [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](nsalert/alertwithmessagetext:defaultbutton:alternatebutton:otherbutton:informativetextwithformat:.md) to create an alert, the following constants are used to identify the button used to dismiss the alert: `NSAlertDefaultReturn`, `NSAlertAlternateReturn`, and `NSAlertOtherReturn`. Otherwise, the constants used are the ones described in `Button Return Values`.

## Parameters

- `window`: The parent window for the sheet.
- `delegate`: The delegate for the modal-dialog session.
- `didEndSelector`: Message the alert sends to   after the user responds but before the sheet is dismissed.
- `contextInfo`: Contextual data passed to   in   message.

## See Also

- [func runModal() -> NSApplication.ModalResponse](nsalert/runmodal.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nsalert/beginsheetmodal(for:completionhandler:).md)
  Runs the alert modally as a sheet attached to the specified window.
- [var suppressionButton: NSButton?](nsalert/suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](nsalert/showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/beginsheetmodal(for:modaldelegate:didend:contextinfo:))*