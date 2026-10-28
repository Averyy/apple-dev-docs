# setShowPanels:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the print operation should display a print panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`showsPrintPanel`](./showsprintpanel.md) and [`showsProgressPanel`](./showsprogresspanel.md) instead.

## Declaration

```objc
- (void) setShowPanels:(BOOL) flag;
```

## Discussion

This method also affects whether a progress panel is presented while the operation runs. If an EPS or PDF copy operation is being performed, neither panel is displayed, regardless of the value of `flag`.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the print operation should display a print panel; otherwise, [`false`](../../Swift/false.md).

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
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/setshowpanels:)*