# runModal()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the page layout panel and begins the modal loop using the shared print info object.

**Availability**:
- macOS

## Declaration

```swift
func runModal() -> Int
```

```objc
- (NSInteger) runModal;
```

## Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise, `NSOKButton`.

## Discussion

The receiver’s values are recorded in the shared `NSPrintInfo` object.

## See Also

### Running the page setup dialog
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](./beginsheet%28using,on,completionhandler%29.md)
- [func runModal(with: NSPrintInfo) -> Int](./runmodal%28with%29.md)
  Displays the page layout panel and begins the modal loop using the specified print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/runmodal())*