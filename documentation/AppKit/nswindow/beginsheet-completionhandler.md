# beginSheet(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Starts a document-modal session and presents—or queues for presentation—a sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func beginSheet(_ sheetWindow: NSWindow) async -> NSApplication.ModalResponse
```

#### Discussion

If the window already has a presented sheet, this method queues the specified sheet for presentation after the current sheet is dismissed and then returns control to the caller.

If the window has no presented sheets, this method displays the specified sheet, makes it key, and returns control to the caller. While the sheet remains visible, most events targeted at the receiver are prohibited.  The runloop does not enter any special mode to accomplish this.

## Parameters

- `sheetWindow`: The window object that represents the sheet to present.
- `handler`: The completion handler that gets called when the sheet’s modal session ends.

## See Also

- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](nswindow/issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginCriticalSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/begincriticalsheet(_:completionhandler:).md)
  Starts a document-modal session and presents the specified critical sheet.
- [func endSheet(NSWindow)](nswindow/endsheet(_:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](nswindow/endsheet(_:returncode:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](nswindow/sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/beginsheet(_:completionhandler:))*