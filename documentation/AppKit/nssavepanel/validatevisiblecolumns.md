# validateVisibleColumns()

**Framework**: AppKit  
**Kind**: method

Validates and reloads the browser columns visible in the panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateVisibleColumns()
```

#### Discussion

Call this method to validate the contents of the panel. For example, you might call it to allow the selection of files with certain extensions based on the selection made in an accessory-view pop-up list. When the user changes the selection, invoke this method to revalidate the visible columns.

## See Also

- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/beginsheetmodal(for:completionhandler:).md)
  Presents the panel as a sheet modal to the specified window.
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/begin(completionhandler:).md)
  Presents the panel as a modeless window.
- [func runModal() -> NSApplication.ModalResponse](nssavepanel/runmodal.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/validatevisiblecolumns())*