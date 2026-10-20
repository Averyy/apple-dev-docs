# recentsMenuItemTag

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The location of recent search strings in the “recents” menu group.

**Availability**:
- macOS

## Declaration

```swift
class var recentsMenuItemTag: Int { get }
```

```c
static const NSInteger NSSearchFieldRecentsMenuItemTag;
```

## See Also

### Managing Menu Templates
- [var searchMenuTemplate: NSMenu?](./searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
- [class var clearRecentsMenuItemTag: Int](./clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class var noRecentsMenuItemTag: Int](./norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class var recentsTitleMenuItemTag: Int](./recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/recentsmenuitemtag)*