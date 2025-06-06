# runModal()

**Framework**: AppKit  
**Kind**: method

Displays the Print panel and begins the modal loop.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal() -> Int
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise `NSOKButton`.

#### Discussion

This method uses the printing information associated with the current printing operation.

## See Also

- [var printInfo: NSPrintInfo](nsprintoperation/printinfo.md)
  The printing information associated with the print operation.
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](nsprintpanel/beginsheet(using:on:completionhandler:).md)
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintpanel/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Displays a Print panel sheet and runs it modally for the specified window.
- [func runModal(with: NSPrintInfo) -> Int](nsprintpanel/runmodal(with:).md)
  Displays the Print panel and runs the modal loop using the specified printing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/runmodal())*