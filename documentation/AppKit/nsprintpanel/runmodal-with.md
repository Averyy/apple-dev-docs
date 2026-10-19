# runModal(with:)

**Framework**: AppKit  
**Kind**: method

Displays the Print panel and runs the modal loop using the specified printing information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal(with printInfo: NSPrintInfo) -> Int
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise `NSOKButton`.

## Parameters

- `printInfo`: The printing information to use while displaying the Print panel.

## See Also

- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](nsprintpanel/beginsheet(using:on:completionhandler:).md)
- [func runModal() -> Int](nsprintpanel/runmodal.md)
  Displays the Print panel and begins the modal loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/runmodal(with:))*