# isSheet

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window has ever run as a modal sheet.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isSheet: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window has ever run as a modal sheet; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/issheet)*