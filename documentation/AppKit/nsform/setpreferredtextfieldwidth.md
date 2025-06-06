# setPreferredTextFieldWidth(_:)

**Framework**: AppKit  
**Kind**: method

Sets the preferred text field width used by Auto Layout.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func setPreferredTextFieldWidth(_ preferredWidth: CGFloat)
```

#### Discussion

The preferred width is reflected in the cell’s [`cellSize`](nscell/cellsize.md), which will be large enough to accommodate the title, bezel, and a text field of width preferredTextWidth. It is also reflected in the [`intrinsicContentSize`](nsview/intrinsiccontentsize.md) of the form. That is, under Auto Layout, the form will try to size itself so that the text field cell is the given width, according to the usual content size constraint priorities.

If the width is negative, the [`cellSize`](nscell/cellsize.md) matches the historic behavior, which is that it is large enough to accommodate the title, bezel, and the current text.

The preferred width is reflected in the cell’s cellSize, which will be large enough to accommodate the title, bezel, and a text field of width [`preferredTextFieldWidth()`](nsform/preferredtextfieldwidth().md).

This method can aid migration to Auto Layout, and is sufficient for simple cases. However, for new apps, use [`NSTextField`](nstextfield.md) objects directly instead of `NSForm`.

The default is -1.

## Parameters

- `preferredWidth`: The preferred width.

## See Also

- [func preferredTextFieldWidth() -> CGFloat](nsform/preferredtextfieldwidth.md)
  The preferred width of the form’s cells when using Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/setpreferredtextfieldwidth(_:))*