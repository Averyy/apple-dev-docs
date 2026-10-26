# setKeyEquivalentFont(_:size:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets by name and size of the font used to draw the key equivalent.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: The keyEquivalentFont property is no longer used. Setting it has no effect.

## Declaration

```swift
func setKeyEquivalentFont(_ fontName: String, size fontSize: CGFloat)
```

```objc
- (void) setKeyEquivalentFont:(NSString *) fontName size:(CGFloat) fontSize;
```

#### Discussion

This method redisplays the button if necessary. It does nothing if the button doesn’t have a key equivalent associated with it. The default font is the same as that used to draw the title.

## Parameters

- `fontName`: The name of the font to use to draw the key equivalent.
- `fontSize`: The font size to use to draw the key equivalent.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
### Deprecated methods
- [- alternateMnemonic](./alternatemnemonic.md)
  Returns the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- alternateMnemonicLocation](./alternatemnemoniclocation.md)
  Returns an unsigned integer indicating the character in the alternate title that’s marked as the “keyboard mnemonic.”
- [- setAlternateMnemonicLocation:](./setalternatemnemoniclocation_.md)
  Sets the character in the alternate title that should be the “keyboard mnemonic.”
- [- setAlternateTitleWithMnemonic:](./setalternatetitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its alternate state to the given string with an embedded mnemonic.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title the button displays when it’s in its normal state to the given string with an embedded mnemonic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setkeyequivalentfont(_:size:))*