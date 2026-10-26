# setTitleWithMnemonic(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title of a menu item with a character denoting an access key.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```swift
func setTitleWithMnemonic(_ stringWithAmpersand: String)
```

```objc
- (void) setTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

#### Discussion

Use an ampersand character to mark the character (the one following the ampersand) to be designated.

## See Also

### Deprecated
- [static func sectionHeader(withTitle: String) -> NSMenuItem](./sectionheader%28withtitle%29.md)
  Returns a menu item representing a section header for a logical grouping of menu commands.
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined character in the menu item title used as a mnemonic.
### Related Documentation
- [- mnemonic](./mnemonic.md)
  Returns the character in the menu item title that appears underlined for use as a mnemonic.
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the menu item title at location that is to be underlined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/settitlewithmnemonic(_:))*