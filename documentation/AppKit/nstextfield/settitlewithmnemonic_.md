# setTitleWithMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the text field’s string value using the embedded character as the keyboard mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`title`](../nscell/title.md) instead.

## Declaration

```objc
- (void) setTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

## Parameters

- `stringWithAmpersand`: The string to set as the title. The system uses the first character that has an ampersand (&) preceding it as the mnemonic, and strips out the ampersand.

## See Also

### Using keyboard interface control
- [var allowsCharacterPickerTouchBarItem: Bool](./allowscharacterpickertouchbaritem.md)
  A Boolean value that controls whether the Touch Bar displays the character picker item for rich text fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/settitlewithmnemonic:)*