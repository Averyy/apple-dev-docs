# suppressionButton

**Framework**: AppKit  
**Kind**: property

The alert’s suppression checkbox.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var suppressionButton: NSButton? { get }
```

#### Discussion

If you want to customize an alert’s suppression checkbox, access it via this property and then use the methods of the [`NSButton`](nsbutton.md) class. For example, you can do this to change the suppression checkbox’s default message, or to change its initial selection state (which is “unselected” by default). For a code example, see the [`showsSuppressionButton`](nsalert/showssuppressionbutton.md) property.

## See Also

- [func runModal() -> NSApplication.ModalResponse](nsalert/runmodal.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nsalert/beginsheetmodal(for:completionhandler:).md)
  Runs the alert modally as a sheet attached to the specified window.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsalert/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the alert modally as an alert sheet attached to a specified window.
- [var showsSuppressionButton: Bool](nsalert/showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/suppressionbutton)*