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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/settitlewithmnemonic(_:))*