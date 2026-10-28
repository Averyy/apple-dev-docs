# validateVisibleColumns()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Validates and reloads the browser columns visible in the panel.

**Availability**:
- macOS

## Declaration

```swift
func validateVisibleColumns()
```

```objc
- (void) validateVisibleColumns;
```

## Discussion

Call this method to validate the contents of the panel. For example, you might call it to allow the selection of files with certain extensions based on the selection made in an accessory-view pop-up list. When the user changes the selection, invoke this method to revalidate the visible columns.

## See Also

### Showing the Panel
- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](./beginsheetmodal%28for,completionhandler%29.md)
  Presents the panel as a sheet modal to the specified window.
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](./begin%28completionhandler%29.md)
  Presents the panel as a modeless window.
- [func runModal() -> NSApplication.ModalResponse](./runmodal%28%29.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/validatevisiblecolumns())*