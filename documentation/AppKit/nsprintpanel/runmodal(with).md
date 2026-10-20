# runModal(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the Print panel and runs the modal loop using the specified printing information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal(with printInfo: NSPrintInfo) -> Int
```

```objc
- (NSInteger) runModalWithPrintInfo:(NSPrintInfo *) printInfo;
```

#### Return Value

`NSCancelButton` if the user clicks the Cancel button; otherwise `NSOKButton`.

## Parameters

- `printInfo`: The printing information to use while displaying the Print panel.

## See Also

### Running the Panel
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](./beginsheet%28using,on,completionhandler%29.md)
- [func runModal() -> Int](./runmodal%28%29.md)
  Displays the Print panel and begins the modal loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/runmodal(with:))*