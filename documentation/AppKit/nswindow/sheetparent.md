# sheetParent

**Framework**: AppKit  
**Kind**: property

The window to which the sheet is attached.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var sheetParent: NSWindow? { get }
```

#### Discussion

The value of this property is `nil` if the receiver is not a sheet or has no sheet parent.

The window object in this property refers to the window to which the sheet is logically attached, regardless of appearance. The parent window–sheet relationship begins with the beginning of the sheet (for example, through [`beginSheet(_:completionHandler:)`](nswindow/beginsheet(_:completionhandler:).md)) and ends with the sheet’s dismissal (for example, through [`endSheet(_:)`](nswindow/endsheet(_:)-4dmmq.md)).

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
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](nswindow/endsheet(_:returncode:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sheetparent)*