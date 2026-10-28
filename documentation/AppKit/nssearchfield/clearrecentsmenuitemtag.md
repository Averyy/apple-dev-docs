# clearRecentsMenuItemTag

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The menu item for clearing the current set of recent string searches in the menu.

**Availability**:
- macOS

## Declaration

```swift
class var clearRecentsMenuItemTag: Int { get }
```

```c
static const NSInteger NSSearchFieldClearRecentsMenuItemTag;
```

## Discussion

This item is hidden if there are no recent strings.

## See Also

### Managing Menu Templates
- [var searchMenuTemplate: NSMenu?](./searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
- [class var noRecentsMenuItemTag: Int](./norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class var recentsMenuItemTag: Int](./recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.
- [class var recentsTitleMenuItemTag: Int](./recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/clearrecentsmenuitemtag)*