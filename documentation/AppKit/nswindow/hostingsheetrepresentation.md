# NSWindow.HostingSheetRepresentation

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A class representing a SwiftUI view hosted in an AppKit sheet.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class HostingSheetRepresentation<Content> where Content : View
```

## Overview

This is created and returned by [`beginSheet(content:completionHandler:)`](./beginsheet%28content,completionhandler%29.md) as a representation of the presented sheet. It can be used to change the root view of the sheet while presented or be used to programamtically dismiss the sheet from an AppKit context using [`endSheet(_:)`](./endsheet%28_%29-6af2u.md).

## Topics

### Instance Properties
- [var rootView: Content](./hostingsheetrepresentation/rootview.md)
  The root view of the sheet.

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
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](./endsheet%28_,returncode%29.md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](./sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](./sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/hostingsheetrepresentation)*