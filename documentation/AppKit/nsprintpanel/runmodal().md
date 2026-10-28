# runModal()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the Print panel and begins the modal loop.

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

`NSCancelButton` if the user clicks the Cancel button; otherwise `NSOKButton`.

## Discussion

This method uses the printing information associated with the current printing operation.

## See Also

### Related Documentation
- [var printInfo: NSPrintInfo](../nsprintoperation/printinfo.md)
  The printing information associated with the print operation.
### Running the Panel
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](./beginsheet%28using,on,completionhandler%29.md)
- [func runModal(with: NSPrintInfo) -> Int](./runmodal%28with%29.md)
  Displays the Print panel and runs the modal loop using the specified printing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/runmodal())*