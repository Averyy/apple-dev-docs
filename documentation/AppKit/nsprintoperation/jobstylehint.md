# jobStyleHint

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The type of content that the print job is printing.

**Availability**:
- macOS 10.2+ - Deprecated in 10.5

> **Deprecated**: Use the [`jobStyleHint`](../nsprintpanel/jobstylehint-swift.property.md) property of [`NSPrintPanel`](../nsprintpanel.md) instead.

## Declaration

```objc
- (NSString *) jobStyleHint;
```

#### Return Value

The content description, or `nil` if no job style hint has been set.

## See Also

### Deprecated methods
- [- setJobStyleHint:](./setjobstylehint_.md)
  Sets the type of content that the print job is printing.
- [- accessoryView](./accessoryview.md)
  Returns the accessory view used by the print operation’s print panel.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the custom accessory view to be displayed by the print operation’s print panel.
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/jobstylehint)*