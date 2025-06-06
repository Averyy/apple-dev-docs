# preferredTextFieldWidth

**Framework**: AppKit  
**Kind**: property

The preferred text field width.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var preferredTextFieldWidth: CGFloat { get set }
```

#### Discussion

The preferred width is reflected in the cell’s `cellSize`, which will be large enough to accommodate the title, bezel, and a text field of width `preferredTextWidth`. It is also reflected in the [`intrinsicContentSize`](nsview/intrinsiccontentsize.md) of the [`NSForm`](nsform.md) object. That is, under Auto Layout, the form will try to size itself so that the text field cell is the given width, according to the usual content size constraint priorities.

If the width is negative, the cel size matches the historic behavior, which is that it is large enough to accommodate the title, bezel, and the current text.

This property can aid migration to Auto Layout, and is sufficient for simple cases. However, for new apps, it’s recommended that you use an [`NSTextField`](nstextfield.md) instance directly instead of a form.

The default value of this property is `-1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/preferredtextfieldwidth)*