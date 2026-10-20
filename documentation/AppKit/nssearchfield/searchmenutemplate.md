# searchMenuTemplate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu object used to dynamically construct the search field’s pop-up icon menu.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var searchMenuTemplate: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * searchMenuTemplate;
```

## See Also

### Related Documentation
- [Search Fields](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/SearchFields.html#//apple_ref/doc/uid/10000168i)
### Managing Menu Templates
- [class var clearRecentsMenuItemTag: Int](./clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class var noRecentsMenuItemTag: Int](./norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class var recentsMenuItemTag: Int](./recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.
- [class var recentsTitleMenuItemTag: Int](./recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/searchmenutemplate)*