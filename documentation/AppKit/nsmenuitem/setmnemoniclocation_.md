# setMnemonicLocation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the character of the menu item title at location that is to be underlined.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This method did nothing useful and there is no replacement.

## Declaration

```objc
- (void) setMnemonicLocation:(NSUInteger) location;
```

#### Discussion

This character identifies the access key by which users can access the menu item.

## Parameters

- `location`: An integer index into the character array of the title. `location` must be from 0 to 254.

## See Also

### Deprecated
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined character in the menu item title used as a mnemonic.
- [func setTitleWithMnemonic(String)](./settitlewithmnemonic%28_%29.md)
  Sets the title of a menu item with a character denoting an access key.
- [- mnemonic](./mnemonic.md)
  Returns the character in the menu item title that appears underlined for use as a mnemonic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/setmnemoniclocation:)*