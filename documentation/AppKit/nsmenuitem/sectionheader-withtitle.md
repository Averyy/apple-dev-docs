# sectionHeader(withTitle:)

**Framework**: AppKit  
**Kind**: method

Returns a menu item representing a section header for a logical grouping of menu commands.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static func sectionHeader(withTitle title: String) -> NSMenuItem
```

#### Discussion

Use section headers to provide context to a group of menu items. Items created using this method are non-interactive and don’t perform actions.

## Parameters

- `title`: The title string to display on the section header.

## See Also

- [func setTitleWithMnemonic(String)](nsmenuitem/settitlewithmnemonic(_:).md)
  Sets the title of a menu item with a character denoting an access key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/sectionheader(withtitle:))*