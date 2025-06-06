# runModal(with:)

**Framework**: AppKit  
**Kind**: method

Displays the Print panel and runs the modal loop using the specified printing information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func runModal(with printInfo: NSPrintInfo) -> Int
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise `NSOKButton`.

## Parameters

- `printInfo`: The printing information to use while displaying the Print panel.

## See Also

- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](nsprintpanel/beginsheet(using:on:completionhandler:).md)
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintpanel/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Displays a Print panel sheet and runs it modally for the specified window.
- [func runModal() -> Int](nsprintpanel/runmodal.md)
  Displays the Print panel and begins the modal loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/runmodal(with:))*