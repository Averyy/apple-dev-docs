# beginSheetModal(for:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents the panel as a sheet modal to the specified window.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func beginSheetModal(for window: NSWindow) async -> NSApplication.ModalResponse
```

#### Discussion

Configure all the relevant properties of the panel before you call this method. The completion handler block runs after the user dismisses the panel, but while the panel may still be onscreen. If you need to dismiss the panel from the screen—for example, if the completion block displays an alert—close the panel by calling its [`orderOut(_:)`](nswindow/orderout(_:).md) method with the value `nil`.

## Parameters

- `window`: The window in which the panel will be presented.
- `handler`: The block called after the user dismisses the panel. The argument passed in will be   if the user chose the OK button or   if the user chose the Cancel button.

## See Also

- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/begin(completionhandler:).md)
  Presents the panel as a modeless window.
- [func runModal() -> NSApplication.ModalResponse](nssavepanel/runmodal.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.
- [func validateVisibleColumns()](nssavepanel/validatevisiblecolumns.md)
  Validates and reloads the browser columns visible in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/beginsheetmodal(for:completionhandler:))*