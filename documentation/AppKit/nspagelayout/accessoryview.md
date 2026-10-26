# accessoryView

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the page layout panel’s accessory view.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Deprecated in OS X v10.5. Use [`accessoryControllers`](./accessorycontrollers.md) instead.

## Declaration

```objc
- (NSView *) accessoryView;
```

## See Also

### Deprecated
- [- setAccessoryView:](./setaccessoryview_.md)
  Adds a view object to the page layout panel.
- [- readPrintInfo](./readprintinfo.md)
  Sets the page layout’s values to those stored in the print info object used when the page layout panel is run.
- [- writePrintInfo](./writeprintinfo.md)
  Writes the page layout’s values to the print info object used when the page layout panel is run.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/accessoryview)*