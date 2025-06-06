# showAllHelpTopics(forSearch:)

**Framework**: AppKit  
**Kind**: method

If this method is implemented, a “Show All Help Topics” item will appear in the menu and this method is called when the user selects it.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func showAllHelpTopics(forSearch searchString: String)
```

#### Discussion

The application should show all its results for this search, which does not include results for menu items.  The string for “Show All Help Topics” is system defined and localized and cannot be changed by the user.

## Parameters

- `searchString`: The search string.

## See Also

- [func localizedTitles(forItem: Any) -> [String]](nsuserinterfaceitemsearching/localizedtitles(foritem:).md)
  Returns an array of localized strings that will form the help menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/showallhelptopics(forsearch:))*