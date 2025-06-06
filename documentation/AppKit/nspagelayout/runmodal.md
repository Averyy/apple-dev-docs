# runModal()

**Framework**: AppKit  
**Kind**: method

Displays the page layout panel and begins the modal loop using the shared print info object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal() -> Int
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise, `NSOKButton`.

#### Discussion

The receiver’s values are recorded in the shared `NSPrintInfo` object.

## See Also

- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](nspagelayout/beginsheet(using:on:completionhandler:).md)
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.
- [func runModal(with: NSPrintInfo) -> Int](nspagelayout/runmodal(with:).md)
  Displays the page layout panel and begins the modal loop using the specified print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/runmodal())*