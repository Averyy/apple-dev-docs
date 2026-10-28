# changeDocumentBackgroundColor(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action method used to set the background color.

**Availability**:
- macOS

## Declaration

```swift
func changeDocumentBackgroundColor(_ sender: Any?)
```

```objc
- (void) changeDocumentBackgroundColor:(id) sender;
```

## Discussion

This method gets the new color by sending a [`color`](../nscolorpanel/color.md) message to  `sender`.

This will only set the background color if [`allowsDocumentBackgroundColorChange`](./allowsdocumentbackgroundcolorchange.md)returns [`true`](../../Swift/true.md).

## Parameters

- `sender`: The control that wants to set the background color.

## See Also

### Setting graphics attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The receiver’s background color.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that indicates whether the receiver draws its background.
- [var allowsDocumentBackgroundColorChange: Bool](./allowsdocumentbackgroundcolorchange.md)
  A Boolean value that indicates whether the receiver allows its background color to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/changedocumentbackgroundcolor(_:))*