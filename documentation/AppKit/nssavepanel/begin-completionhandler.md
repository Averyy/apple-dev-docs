# begin(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents the panel as a modeless window.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func begin() async -> NSApplication.ModalResponse
```

#### Discussion

Configure all of the relevant properties of the panel before you call this method.

## Parameters

- `handler`: The block to call after the user closes the panel. This block has no return value and takes a single parameter:

## See Also

- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/beginsheetmodal(for:completionhandler:).md)
  Presents the panel as a sheet modal to the specified window.
- [func runModal() -> NSApplication.ModalResponse](nssavepanel/runmodal.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.
- [func validateVisibleColumns()](nssavepanel/validatevisiblecolumns.md)
  Validates and reloads the browser columns visible in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/begin(completionhandler:))*