# sectionHeaderWithTitle:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a menu item representing a section header for a logical grouping of menu commands.

**Availability**:
- macOS 14.0+

## Declaration

```objc
+ (instancetype) sectionHeaderWithTitle:(NSString *) title;
```

## Return Value

A menu item representing a section header for a logical grouping of menu commands.

## Discussion

Use section headers to provide context to a group of menu items. Items created using this method are non-interactive and don’t perform actions.

## Parameters

- `title`: The title string to display on the section header.

## See Also

### Managing the section header
- [var isSectionHeader: Bool](./issectionheader.md)
  A Boolean value indicating whether the menu item is a section header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/sectionheaderwithtitle:)*