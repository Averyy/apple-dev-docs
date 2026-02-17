# recentsTitleMenuItemTag

**Framework**: AppKit  
**Kind**: property

The menu item that provides the title of the menu group for recent search strings.

**Availability**:
- macOS ?+

## Declaration

```swift
class var recentsTitleMenuItemTag: Int { get }
```

#### Discussion

This item is hidden if there are no recent strings.

You may use this tagged item for separator characters that also don’t appear if there are no recent strings to display.

## See Also

- [var searchMenuTemplate: NSMenu?](nssearchfield/searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
- [class var clearRecentsMenuItemTag: Int](nssearchfield/clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class var noRecentsMenuItemTag: Int](nssearchfield/norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class var recentsMenuItemTag: Int](nssearchfield/recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/recentstitlemenuitemtag)*