# runModal()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.

**Availability**:
- macOS

## Declaration

```swift
func runModal() -> NSApplication.ModalResponse
```

```objc
- (NSModalResponse) runModal;
```

## Return Value

`NSFileHandlingPanelOKButton` (if the user clicks the OK button) or `NSFileHandlingPanelCancelButton` (if the user clicks the Cancel button).

## Discussion

This method invokes `NSApplication`’s [`runModal(for:)`](../nsapplication/runmodal%28for%29.md) method with `self` as the argument.

## See Also

### Related Documentation
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](../nsapplication/runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
### Showing the Panel
- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](./beginsheetmodal%28for,completionhandler%29.md)
  Presents the panel as a sheet modal to the specified window.
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](./begin%28completionhandler%29.md)
  Presents the panel as a modeless window.
- [func validateVisibleColumns()](./validatevisiblecolumns%28%29.md)
  Validates and reloads the browser columns visible in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/runmodal())*