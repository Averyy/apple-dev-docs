# endSheet(_:returnCode:)

**Framework**: AppKit  
**Kind**: method

Ends a document-modal session and dismisses the specified sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func endSheet(_ sheetWindow: NSWindow, returnCode: NSApplication.ModalResponse)
```

#### Discussion

This method ends the modal session with the specified return code.

## Parameters

- `sheetWindow`: The window object that represents the sheet to dismiss.
- `returnCode`: The return code to send to the completion handler. You can use  a custom value that you define or one of the return codes defined in the   enumeration or   .

## See Also

- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](nswindow/issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/beginsheet(_:completionhandler:).md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func beginCriticalSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/begincriticalsheet(_:completionhandler:).md)
  Starts a document-modal session and presents the specified critical sheet.
- [func endSheet(NSWindow)](nswindow/endsheet(_:)-4dmmq.md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](nswindow/sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/endsheet(_:returncode:))*