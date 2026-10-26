# alternateMnemonicLocation

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an unsigned integer indicating the character in the alternate title that’s marked as the “keyboard mnemonic.”

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (NSUInteger) alternateMnemonicLocation;
```

#### Return Value

An unsigned integer indicating the character in the alternate title (the title displayed on the button when it’s in its alternate state) that’s marked as the “keyboard mnemonic.” If the alternate title doesn’t have a keyboard mnemonic, returns `NSNotFound`.

#### Discussion

Mnemonics are not supported in macOS.

## See Also

### Related Documentation
- [- mnemonicLocation](../nscell/mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.
### Deprecated methods
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- setAlternateMnemonicLocation:](./setalternatemnemoniclocation_.md)
  Sets the character in the alternate title that should be the “keyboard mnemonic.”
- [- setAlternateTitleWithMnemonic:](./setalternatetitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.
- [func setKeyEquivalentFont(String, size: CGFloat)](./setkeyequivalentfont%28_,size%29.md)
  Sets by name and size of the font used to draw the key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/alternatemnemoniclocation)*