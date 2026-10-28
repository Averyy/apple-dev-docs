# mnemonicLocation

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the position of the underlined character in the menu item title used as a mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This method did nothing useful and there is no replacement.

## Declaration

```objc
- (NSUInteger) mnemonicLocation;
```

## Discussion

The position is the zero-based index of that character in the title string. If the receiver has no mnemonic character, returns `NSNotFound`.

## See Also

### Deprecated
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the menu item title at location that is to be underlined.
- [func setTitleWithMnemonic(String)](./settitlewithmnemonic%28_%29.md)
  Sets the title of a menu item with a character denoting an access key.
- [- mnemonic](./mnemonic.md)
  Returns the character in the menu item title that appears underlined for use as a mnemonic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/mnemoniclocation)*