# searchMenuTemplate

**Framework**: AppKit  
**Kind**: property

The menu object used to dynamically construct the search field’s pop-up icon menu.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var searchMenuTemplate: NSMenu? { get set }
```

## See Also

- [Search Fields](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/SearchFields.html#//apple_ref/doc/uid/10000168i)
- [class let clearRecentsMenuItemTag: Int](nssearchfield/clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class let noRecentsMenuItemTag: Int](nssearchfield/norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class let recentsMenuItemTag: Int](nssearchfield/recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.
- [class let recentsTitleMenuItemTag: Int](nssearchfield/recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/searchmenutemplate)*