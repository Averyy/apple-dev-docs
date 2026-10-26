# setAccessoryView:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a view object to the page layout panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Deprecated in OS X v10.5. Use [`addAccessoryController(_:)`](./addaccessorycontroller%28_%29.md) instead.

## Declaration

```objc
- (void) setAccessoryView:(NSView *) accessoryView;
```

#### Discussion

Invoke this method to add a custom view containing your controls. `aView` is added to the receiver’s Settings popup menu with your application’s name as its menu item. The receiver is automatically resized to accommodate `aView`. This method can be invoked repeatedly to change the accessory view depending on the situation. If `aView` is `nil`, then the receiver’s current accessory view, if any, is removed.

## See Also

### Deprecated
- [- accessoryView](./accessoryview.md)
  Returns the page layout panel’s accessory view.
- [- readPrintInfo](./readprintinfo.md)
  Sets the page layout’s values to those stored in the print info object used when the page layout panel is run.
- [- writePrintInfo](./writeprintinfo.md)
  Writes the page layout’s values to the print info object used when the page layout panel is run.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/setaccessoryview:)*