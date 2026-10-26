# title

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title displayed on the button when it’s in its normal state.

**Availability**:
- macOS

## Declaration

```swift
var title: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * title;
```

#### Discussion

If the button doesn’t display a title, the value of this property is the empty string. This title is always displayed if the button doesn’t use its alternate contents for highlighting or displaying the alternate state. By default, a button’s title is “Button.” Setting this property may redraw the button if necessary.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.
- [- mnemonicLocation](../nscell/mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.
- [- mnemonic](../nscell/mnemonic.md)
  Returns the character in the receiver’s title that appears underlined for use as a mnemonic.
### Setting Titles
- [var alternateTitle: String](./alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [var attributedAlternateTitle: NSAttributedString](./attributedalternatetitle.md)
  The title displayed by the button when it’s in its alternate state, as an attributed string.
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/title)*