# beginSheet(using:on:completionHandler:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPrintPanel.Result
```

#### Discussion

## See Also

- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintpanel/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Displays a Print panel sheet and runs it modally for the specified window.
- [func runModal() -> Int](nsprintpanel/runmodal.md)
  Displays the Print panel and begins the modal loop.
- [func runModal(with: NSPrintInfo) -> Int](nsprintpanel/runmodal(with:).md)
  Displays the Print panel and runs the modal loop using the specified printing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/beginsheet(using:on:completionhandler:))*