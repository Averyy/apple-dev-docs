# endSheet(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends a document-modal session and dismisses the specified sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func endSheet(_ sheetWindow: NSWindow)
```

```objc
- (void) endSheet:(NSWindow *) sheetWindow;
```

## Discussion

This method ends the modal session with the return code `NSModalResponseStop`.

## Parameters

- `sheetWindow`: The window object that represents the sheet to be dismissed.

## See Also

### Managing Sheets
- [var attachedSheet: NSWindow?](./attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](./issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./beginsheet%28_,completionhandler%29.md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func beginSheet<V>(content: () -> V, completionHandler: (() -> Void)?) -> NSWindow.HostingSheetRepresentation<V>](./beginsheet%28content,completionhandler%29.md)
  Presents a SwiftUI view as a sheet on the receiving NSWindow.
- [func beginCriticalSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./begincriticalsheet%28_,completionhandler%29.md)
  Starts a document-modal session and presents the specified critical sheet.
- [func endSheet<V>(NSWindow.HostingSheetRepresentation<V>)](./endsheet%28_%29-6af2u.md)
  Ends a SwiftUI hosted sheet presentation.
- [NSWindow.HostingSheetRepresentation](./hostingsheetrepresentation.md)
  A class representing a SwiftUI view hosted in an AppKit sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](./endsheet%28_,returncode%29.md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](./sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](./sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/endsheet(_:)-4dmmq)*