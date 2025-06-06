# noRecentsMenuItemTag

**Framework**: AppKit  
**Kind**: property

The menu item that describes a lack of recent search strings.

**Availability**:
- macOS ?+

## Declaration

```swift
class let noRecentsMenuItemTag: Int
```

#### Discussion

This item is hidden if there have been recent searches.

## See Also

- [var searchMenuTemplate: NSMenu?](nssearchfield/searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
- [class let clearRecentsMenuItemTag: Int](nssearchfield/clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class let recentsMenuItemTag: Int](nssearchfield/recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.
- [class let recentsTitleMenuItemTag: Int](nssearchfield/recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/norecentsmenuitemtag)*