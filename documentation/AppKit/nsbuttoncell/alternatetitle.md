# alternateTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The string displayed by the button when it’s in its alternate state.

**Availability**:
- macOS

## Declaration

```swift
var alternateTitle: String { get set }
```

```objc
@property (copy) NSString * alternateTitle;
```

#### Discussion

The value of this property is the string that appears on the button when it’s in its alternate state, or the empty string if the button doesn’t display an alternate title. Note that some button types don’t display an alternate title. By default, a button’s alternate title is “Button.”

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
### Setting Titles
- [var attributedAlternateTitle: NSAttributedString](./attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var title: String!](./title.md)
  The title displayed on the button when it’s in its normal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/alternatetitle)*