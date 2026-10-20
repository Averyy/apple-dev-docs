# beginSheetModal(for:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the alert modally as a sheet attached to the specified window.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func beginSheetModal(for sheetWindow: NSWindow, completionHandler handler: ((NSApplication.ModalResponse) -> Void)? = nil)
```

```swift
func beginSheetModal(for sheetWindow: NSWindow) async -> NSApplication.ModalResponse
```

```objc
- (void) beginSheetModalForWindow:(NSWindow *) sheetWindow completionHandler:(void (^)(NSModalResponse returnCode)) handler;
```

#### Discussion

This method uses the `NSWindow` sheet methods to display the alert (for more information, see Managing Sheets). If the alert has an alert style of [`NSCriticalAlertStyle`](../nscriticalalertstyle.md), it is presented as a critical sheet, which means that it can display on top of other sheets that might already be attached to the window. Otherwise, it is presented—or queued for presentation—as a standard sheet.

Note that [`orderOut(_:)`](../nswindow/orderout%28_%29.md) no longer needs to be called in the completion handler. If you don’t dismiss the alert, it will be done for you after the completion handler finishes.

## Parameters

- `sheetWindow`: The window on which to display the sheet.
- `handler`: The completion handler that gets called when the sheet’s modal session ends.

## See Also

### Displaying alerts
- [func runModal() -> NSApplication.ModalResponse](./runmodal%28%29.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [var suppressionButton: NSButton?](./suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](./showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the alert modally as an alert sheet attached to a specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/beginsheetmodal(for:completionhandler:))*