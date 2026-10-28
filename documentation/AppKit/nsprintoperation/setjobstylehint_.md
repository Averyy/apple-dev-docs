# setJobStyleHint:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the type of content that the print job is printing.

**Availability**:
- macOS 10.2+ - Deprecated in 10.5

> **Deprecated**: Use the [`jobStyleHint`](../nsprintpanel/jobstylehint-swift.property.md) property of [`NSPrintPanel`](../nsprintpanel.md) instead.

## Declaration

```objc
- (void) setJobStyleHint:(NSString *) hint;
```

## Discussion

This controls the set of items that appear in the Presets menu of the simplified Print panel interface presented by this operation, if it presents one.

## Parameters

- `hint`: A supported job style hint. Valid values for this parameter are described in the `Constants` section of the `NSPrintPanel` class. If this value is `nil`, the standard interface is used.

## See Also

### Deprecated methods
- [- jobStyleHint](./jobstylehint.md)
  The type of content that the print job is printing.
- [- accessoryView](./accessoryview.md)
  Returns the accessory view used by the print operation’s print panel.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the custom accessory view to be displayed by the print operation’s print panel.
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/setjobstylehint:)*