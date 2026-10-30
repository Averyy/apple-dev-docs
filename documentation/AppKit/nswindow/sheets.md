# sheets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the sheets currently attached to the window.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var sheets: [NSWindow] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSWindow *> * sheets;
```

## Discussion

The value of this property is an ordered array that contains—in top-to-bottom order—the presented sheets that are attached to the window, followed by queued sheets, in the order they were queued. The array doesn’t include nested sheets or subsheets.

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
- [func endSheet(NSWindow)](./endsheet%28_%29-4dmmq.md)
  Ends a document-modal session and dismisses the specified sheet.
- [func endSheet<V>(NSWindow.HostingSheetRepresentation<V>)](./endsheet%28_%29-6af2u.md)
  Ends a SwiftUI hosted sheet presentation.
- [NSWindow.HostingSheetRepresentation](./hostingsheetrepresentation.md)
  A class representing a SwiftUI view hosted in an AppKit sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](./endsheet%28_,returncode%29.md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](./sheetparent.md)
  The window to which the sheet is attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sheets)*