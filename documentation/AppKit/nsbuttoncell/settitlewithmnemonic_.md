# setTitleWithMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

## Discussion

If necessary, [`setTitleWithMnemonic:`](./settitlewithmnemonic_.md) redraws the button cell. Mnemonics are not supported in macOS.

## Parameters

- `stringWithAmpersand`: The string to set as the button’s title, taking into account the fact that an embedded “&” character is not a literal but instead marks the alternate state’s “keyboard mnemonic.” This title is always shown on buttons that don’t use their alternate contents when highlighting or displaying their alternate state.

## See Also

### Related Documentation
- [- setMnemonicLocation:](../nscell/setmnemoniclocation_.md)
  Sets the character of the receiver’s title to be used as a mnemonic character.
- [- setTitleWithMnemonic:](../nscell/settitlewithmnemonic_.md)
  Sets the title of the receiver with one character in the string denoted as an access key.
### Deprecated methods
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- alternateMnemonicLocation](./alternatemnemoniclocation.md)
  Returns an unsigned integer indicating the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- setAlternateMnemonicLocation:](./setalternatemnemoniclocation_.md)
  Sets the character in the alternate title that should be the “keyboard mnemonic.”
- [- setAlternateTitleWithMnemonic:](./setalternatetitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.
- [func setKeyEquivalentFont(String, size: CGFloat)](./setkeyequivalentfont%28_,size%29.md)
  Sets by name and size of the font used to draw the key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/settitlewithmnemonic:)*