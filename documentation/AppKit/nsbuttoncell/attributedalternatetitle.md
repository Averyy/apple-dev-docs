# attributedAlternateTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title displayed by the button when it’s in its alternate state, as an attributed string.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var attributedAlternateTitle: NSAttributedString { get set }
```

```objc
@property (copy) NSAttributedString * attributedAlternateTitle;
```

## Discussion

The value of this property is the attributed string that appears on the button when it’s in its alternate state, or the empty string if the button doesn’t display an alternate title. Note that some button types don’t display an alternate title. By default, a button’s alternate title is “Button.”

Graphics attributes that are set on the cell (such as `backgroundColor`, `alignment`, `font`, and so on) are overridden when corresponding properties are set for the attributed string.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
- [- setAlternateMnemonicLocation:](./setalternatemnemoniclocation_.md)
  Sets the character in the alternate title that should be the “keyboard mnemonic.”
- [- setAlternateTitleWithMnemonic:](./setalternatetitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
### Setting Titles
- [var alternateTitle: String](./alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var title: String!](./title.md)
  The title displayed on the button when it’s in its normal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/attributedalternatetitle)*