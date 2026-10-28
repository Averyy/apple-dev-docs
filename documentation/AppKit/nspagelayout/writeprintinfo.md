# writePrintInfo

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the page layout’s values to the print info object used when the page layout panel is run.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Deprecated in OS X v10.5. This method should not be invoked directly, so there is no replacement.

## Declaration

```objc
- (void) writePrintInfo;
```

## Discussion

Do not invoke this method directly; it is invoked automatically when the receiver is dismissed.

## See Also

### Related Documentation
- [var printInfo: NSPrintInfo?](./printinfo.md)
  The printing information object used when the page layout panel is run.
- [func runModal() -> Int](./runmodal%28%29.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](./runmodal%28with%29.md)
  Displays the page layout panel and begins the modal loop using the specified print info object.
### Deprecated
- [- accessoryView](./accessoryview.md)
  Returns the page layout panel’s accessory view.
- [- setAccessoryView:](./setaccessoryview_.md)
  Adds a view object to the page layout panel.
- [- readPrintInfo](./readprintinfo.md)
  Sets the page layout’s values to those stored in the print info object used when the page layout panel is run.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/writeprintinfo)*