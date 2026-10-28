# runModal(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the page layout panel and begins the modal loop using the specified print info object.

**Availability**:
- macOS

## Declaration

```swift
func runModal(with printInfo: NSPrintInfo) -> Int
```

```objc
- (NSInteger) runModalWithPrintInfo:(NSPrintInfo *) printInfo;
```

## Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise, `NSOKButton`.

## Discussion

The receiver’s values are recorded in `printInfo`.

## Parameters

- `printInfo`: The `NSPrintInfo` object to use.

## See Also

### Running the page setup dialog
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](./beginsheet%28using,on,completionhandler%29.md)
- [func runModal() -> Int](./runmodal%28%29.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/runmodal(with:))*