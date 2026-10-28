# sectionHeader(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a menu item representing a section header for a logical grouping of menu commands.

**Availability**:
- macOS 14.0+

> **Deprecated**: Use [`sectionHeader(title:)`](./sectionheader%28title%29.md) instead.

## Declaration

```swift
static func sectionHeader(withTitle title: String) -> NSMenuItem
```

## Discussion

Use section headers to provide context to a group of menu items. Items created using this method are non-interactive and don’t perform actions.

## Parameters

- `title`: The title string to display on the section header.

## See Also

### Deprecated
- [func setTitleWithMnemonic(String)](./settitlewithmnemonic%28_%29.md)
  Sets the title of a menu item with a character denoting an access key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/sectionheader(withtitle:))*