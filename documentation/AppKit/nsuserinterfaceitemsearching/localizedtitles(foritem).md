# localizedTitles(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an array of localized strings that will form the help menu item.

**Availability**:
- macOS

## Declaration

```swift
func localizedTitles(forItem item: Any) -> [String]
```

```objc
- (NSArray<NSString *> *) localizedTitlesForItem:(id) item;
```

#### Return Value

An `NSArray` of `NSStrings` (localized for display in the menu) that will be combined with separators to form the menu item title.

## Parameters

- `item`: At item in the help menu.

## See Also

### Show Help Menu
- [func showAllHelpTopics(forSearch: String)](./showallhelptopics%28forsearch%29.md)
  If this method is implemented, a “Show All Help Topics” item will appear in the menu and this method is called when the user selects it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/localizedtitles(foritem:))*