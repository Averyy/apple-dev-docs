# runModal(for:completionHandler:)

**Framework**: Collaboration  
**Kind**: method

Runs the identity picker modally as a sheet attached to a specified window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal(for window: NSWindow) async -> NSApplication.ModalResponse
```

## Parameters

- `window`: The parent window for the sheet.
- `completionHandler`: The handler to run after the return value is known, but before the sheet is dismissed.

## See Also

- [func runModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](cbidentitypicker/runmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the receiver modally as a sheet attached to a specified window.
- [func runModal() -> Int](cbidentitypicker/runmodal.md)
  Runs the receiver as an application-modal dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/runmodal(for:completionhandler:))*