# showAllHelpTopics(forSearch:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

If this method is implemented, a “Show All Help Topics” item will appear in the menu and this method is called when the user selects it.

**Availability**:
- macOS

## Declaration

```swift
optional func showAllHelpTopics(forSearch searchString: String)
```

```objc
- (void) showAllHelpTopicsForSearchString:(NSString *) searchString;
```

#### Discussion

The application should show all its results for this search, which does not include results for menu items.  The string for “Show All Help Topics” is system defined and localized and cannot be changed by the user.

## Parameters

- `searchString`: The search string.

## See Also

### Show Help Menu
- [func localizedTitles(forItem: Any) -> [String]](./localizedtitles%28foritem%29.md)
  Returns an array of localized strings that will form the help menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/showallhelptopics(forsearch:))*