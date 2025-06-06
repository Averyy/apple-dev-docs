# title

**Framework**: AppKit  
**Kind**: property

The title displayed on the button when it’s in its normal state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var title: String! { get set }
```

#### Discussion

If the button doesn’t display a title, the value of this property is the empty string. This title is always displayed if the button doesn’t use its alternate contents for highlighting or displaying the alternate state. By default, a button’s title is “Button.” Setting this property may redraw the button if necessary.

## See Also

- [var font: NSFont?](nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var alternateTitle: String](nsbuttoncell/alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedAlternateTitle: NSAttributedString](nsbuttoncell/attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var attributedTitle: NSAttributedString](nsbuttoncell/attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/title)*