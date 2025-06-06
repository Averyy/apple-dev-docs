# beginSheet(using:on:completionHandler:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPageLayout.Result
```

## See Also

- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.
- [func runModal() -> Int](nspagelayout/runmodal.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](nspagelayout/runmodal(with:).md)
  Displays the page layout panel and begins the modal loop using the specified print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/beginsheet(using:on:completionhandler:))*