# changeDocumentBackgroundColor(_:)

**Framework**: AppKit  
**Kind**: method

An action method used to set the background color.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeDocumentBackgroundColor(_ sender: Any?)
```

#### Discussion

This method gets the new color by sending a [`color`](nscolorpanel/color.md) message to  `sender`.

This will only set the background color if [`allowsDocumentBackgroundColorChange`](nstextview/allowsdocumentbackgroundcolorchange.md)returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `sender`: The control that wants to set the background color.

## See Also

- [var backgroundColor: NSColor](nstextview/backgroundcolor.md)
  The receiver’s background color.
- [var drawsBackground: Bool](nstextview/drawsbackground.md)
  A Boolean value that indicates whether the receiver draws its background.
- [var allowsDocumentBackgroundColorChange: Bool](nstextview/allowsdocumentbackgroundcolorchange.md)
  A Boolean value that indicates whether the receiver allows its background color to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/changedocumentbackgroundcolor(_:))*