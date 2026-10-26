# showPanels

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the print panel is to be displayed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`showsPrintPanel`](./showsprintpanel.md) and [`showsProgressPanel`](./showsprogresspanel.md) instead.

## Declaration

```objc
- (BOOL) showPanels;
```

#### Return Value

[`true`](../../Swift/true.md) if the print panel is to be displayed; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var printPanel: NSPrintPanel](./printpanel.md)
  The print panel object to use during the operation.
### Deprecated methods
- [- jobStyleHint](./jobstylehint.md)
  The type of content that the print job is printing.
- [- setJobStyleHint:](./setjobstylehint_.md)
  Sets the type of content that the print job is printing.
- [- accessoryView](./accessoryview.md)
  Returns the accessory view used by the print operation’s print panel.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the custom accessory view to be displayed by the print operation’s print panel.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/showpanels)*