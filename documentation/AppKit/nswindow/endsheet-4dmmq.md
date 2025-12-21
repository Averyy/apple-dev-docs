# endSheet(_:)

**Framework**: AppKit  
**Kind**: method

Ends a document-modal session and dismisses the specified sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func endSheet(_ sheetWindow: NSWindow)
```

#### Discussion

This method ends the modal session with the return code `NSModalResponseStop`.

## Parameters

- `sheetWindow`: The window object that represents the sheet to be dismissed.

## See Also

- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](nswindow/issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/beginsheet(_:completionhandler:).md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func beginCriticalSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/begincriticalsheet(_:completionhandler:).md)
  Starts a document-modal session and presents the specified critical sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](nswindow/endsheet(_:returncode:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](nswindow/sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/endsheet(_:)-4dmmq)*