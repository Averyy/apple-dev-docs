# accessoryView

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessory view used by the print operation’s print panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use the [`accessoryControllers`](../nsprintpanel/accessorycontrollers.md) property of [`NSPrintPanel`](../nsprintpanel.md) instead.

## Declaration

```objc
- (NSView *) accessoryView;
```

## Return Value

The custom accessory view.

## Discussion

You use the [`setAccessoryView:`](./setaccessoryview_.md) method to customize the default `NSPrintPanel` object without having to subclass `NSPrintPanel` or specify your own print panel object.

## See Also

### Related Documentation
- [var printPanel: NSPrintPanel](./printpanel.md)
  The print panel object to use during the operation.
### Deprecated methods
- [- jobStyleHint](./jobstylehint.md)
  The type of content that the print job is printing.
- [- setJobStyleHint:](./setjobstylehint_.md)
  Sets the type of content that the print job is printing.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the custom accessory view to be displayed by the print operation’s print panel.
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/accessoryview)*