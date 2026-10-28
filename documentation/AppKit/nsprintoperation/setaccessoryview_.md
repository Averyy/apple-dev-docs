# setAccessoryView:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the custom accessory view to be displayed by the print operation’s print panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use the [`addAccessoryController(_:)`](../nsprintpanel/addaccessorycontroller%28_%29.md) method of [`NSPrintPanel`](../nsprintpanel.md) instead.

## Declaration

```objc
- (void) setAccessoryView:(NSView *) view;
```

## Discussion

You can use this method to avoid subclassing `NSPrintPanel` or specifying your own print panel object. The print panel is automatically resized (as needed) to accommodate the accessory view when it is selected.

## Parameters

- `view`: The view to display in the print panel. You can use this view to specify additional print options.

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
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/setaccessoryview:)*