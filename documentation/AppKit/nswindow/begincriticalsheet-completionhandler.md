# beginCriticalSheet(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Starts a document-modal session and presents the specified critical sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func beginCriticalSheet(_ sheetWindow: NSWindow) async -> NSApplication.ModalResponse
```

#### Discussion

This method displays the sheet—on top of the window’s current sheet, if one exists—makes it key and returns control to the caller. While the sheet remains visible, most events targeted at the receiver are prohibited. The runloop does not enter any special mode to accomplish this.

If the window already has a sheet when this method runs, the existing sheet is temporarily disabled while the critical sheet is presented. When the critical sheet is dismissed, the previously presented sheet continues its standard operation.

## Parameters

- `sheetWindow`: The window object that represents the critical sheet to present. A critical sheet contains content that is time-critical or very important to the user.
- `handler`: The completion handler that gets called when the sheet’s modal session ends.

## See Also

- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](nswindow/issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/beginsheet(_:completionhandler:).md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func endSheet(NSWindow)](nswindow/endsheet(_:)-4dmmq.md)
  Ends a document-modal session and dismisses the specified sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](nswindow/endsheet(_:returncode:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](nswindow/sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/begincriticalsheet(_:completionhandler:))*