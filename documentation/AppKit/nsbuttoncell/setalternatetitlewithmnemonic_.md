# setAlternateTitleWithMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setAlternateTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

#### Discussion

Mnemonics are not supported in macOS.

If necessary, [`setAlternateTitleWithMnemonic:`](./setalternatetitlewithmnemonic_.md) redraws the button cell. Note that some button types don’t display an alternate title.

## Parameters

- `stringWithAmpersand`: The string to set as the button’s alternate title, taking into account the fact that an embedded “&” character is not a literal but instead marks the alternate state’s “keyboard mnemonic.”

## See Also

### Deprecated methods
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- alternateMnemonicLocation](./alternatemnemoniclocation.md)
  Returns an unsigned integer indicating the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- setAlternateMnemonicLocation:](./setalternatemnemoniclocation_.md)
  Sets the character in the alternate title that should be the “keyboard mnemonic.”
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.
- [func setKeyEquivalentFont(String, size: CGFloat)](./setkeyequivalentfont%28_,size%29.md)
  Sets by name and size of the font used to draw the key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setalternatetitlewithmnemonic:)*