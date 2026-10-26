# mnemonic

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the character in the menu item title that appears underlined for use as a mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This method did nothing useful and there is no replacement.

## Declaration

```objc
- (NSString *) mnemonic;
```

#### Discussion

If there is no mnemonic character, returns an empty string.

## See Also

### Deprecated
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the menu item title at location that is to be underlined.
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined character in the menu item title used as a mnemonic.
- [func setTitleWithMnemonic(String)](./settitlewithmnemonic%28_%29.md)
  Sets the title of a menu item with a character denoting an access key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/mnemonic)*