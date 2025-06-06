# runModal()

**Framework**: AppKit  
**Kind**: method

Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal() -> NSApplication.ModalResponse
```

#### Return Value

`NSFileHandlingPanelOKButton` (if the user clicks the OK button) or `NSFileHandlingPanelCancelButton` (if the user clicks the Cancel button).

#### Discussion

This method invokes `NSApplication`’s [`runModal(for:)`](nsapplication/runmodal(for:).md) method with `self` as the argument.

## See Also

- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/beginsheetmodal(for:completionhandler:).md)
  Presents the panel as a sheet modal to the specified window.
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/begin(completionhandler:).md)
  Presents the panel as a modeless window.
- [func validateVisibleColumns()](nssavepanel/validatevisiblecolumns.md)
  Validates and reloads the browser columns visible in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/runmodal())*