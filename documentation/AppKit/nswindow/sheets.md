# sheets

**Framework**: AppKit  
**Kind**: property

An array of the sheets currently attached to the window.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var sheets: [NSWindow] { get }
```

#### Discussion

The value of this property is an ordered array that contains—in top-to-bottom order—the presented sheets that are attached to the window, followed by queued sheets, in the order they were queued. The array doesn’t include nested sheets or subsheets.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sheets)*