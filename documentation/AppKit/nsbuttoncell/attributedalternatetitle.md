# attributedAlternateTitle

**Framework**: AppKit  
**Kind**: property

The title displayed by the button when it’s in its alternate state, as an attributed string.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var attributedAlternateTitle: NSAttributedString { get set }
```

#### Discussion

The value of this property is the attributed string that appears on the button when it’s in its alternate state, or the empty string if the button doesn’t display an alternate title. Note that some button types don’t display an alternate title. By default, a button’s alternate title is “Button.”

Graphics attributes that are set on the cell (such as `backgroundColor`, `alignment`, `font`, and so on) are overridden when corresponding properties are set for the attributed string.

## See Also

- [var font: NSFont?](nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var alternateTitle: String](nsbuttoncell/alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedTitle: NSAttributedString](nsbuttoncell/attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var title: String!](nsbuttoncell/title.md)
  The title displayed on the button when it’s in its normal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/attributedalternatetitle)*