# attributedTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title displayed by the button when it’s in its normal state as an attributed string.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString { get set }
```

```objc
@property (copy) NSAttributedString * attributedTitle;
```

#### Discussion

The value of this property is the attributes string that appears on the button when it’s in its normal state, or an empty attributed string if the button doesn’t display a title. A button’s title is always displayed if the button doesn’t use its alternate contents for highlighting or displaying the alternate state. By default, a button’s title is “Button.” Setting this property redraws the button if necessary.

Graphics attributes configured for the cell (such as `backgroundColor`, `alignment`, `font`, and so on) are overridden when corresponding properties are set for the attributed string.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
### Setting Titles
- [var alternateTitle: String](./alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedAlternateTitle: NSAttributedString](./attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var title: String!](./title.md)
  The title displayed on the button when it’s in its normal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/attributedtitle)*