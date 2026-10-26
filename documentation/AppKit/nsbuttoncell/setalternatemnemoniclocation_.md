# setAlternateMnemonicLocation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the character in the alternate title that should be the “keyboard mnemonic.”

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setAlternateMnemonicLocation:(NSUInteger) location;
```

#### Discussion

Mnemonics are not supported in macOS.

The [`setAlternateMnemonicLocation:`](./setalternatemnemoniclocation_.md) method doesn’t cause the button cell to be redisplayed.

## Parameters

- `location`: An unsigned integer indicating the character in the alternate title that should be marked as the “keyboard mnemonic.” If you don’t want the alternate title to have a keyboard mnemonic, specify a location of `NSNotFound`.

## See Also

### Deprecated methods
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- alternateMnemonicLocation](./alternatemnemoniclocation.md)
  Returns an unsigned integer indicating the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- setAlternateTitleWithMnemonic:](./setalternatetitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.
- [func setKeyEquivalentFont(String, size: CGFloat)](./setkeyequivalentfont%28_,size%29.md)
  Sets by name and size of the font used to draw the key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setalternatemnemoniclocation:)*