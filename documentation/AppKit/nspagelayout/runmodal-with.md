# runModal(with:)

**Framework**: AppKit  
**Kind**: method

Displays the page layout panel and begins the modal loop using the specified print info object.

**Availability**:
- macOS ?+

## Declaration

```swift
func runModal(with printInfo: NSPrintInfo) -> Int
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise, `NSOKButton`.

#### Discussion

The receiver’s values are recorded in `printInfo`.

## Parameters

- `printInfo`: The `NSPrintInfo` object to use.

## See Also

- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](nspagelayout/beginsheet(using:on:completionhandler:).md)
- [func runModal() -> Int](nspagelayout/runmodal.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/runmodal(with:))*