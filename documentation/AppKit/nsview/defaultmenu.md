# defaultMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Overridden by subclasses to return the default pop-up menu for instances of the receiving class.

**Availability**:
- macOS

## Declaration

```swift
class var defaultMenu: NSMenu? { get }
```

```objc
@property (class, strong, readonly, nullable) NSMenu * defaultMenu;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

The default implementation returns `nil`.

## See Also

### Related Documentation
- [var menu: NSMenu?](../nsresponder/menu.md)
  Returns the responder’s menu.
### Managing Contextual Menus
- [func menu(for: NSEvent) -> NSMenu?](./menu%28for%29.md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [func willOpenMenu(NSMenu, with: NSEvent)](./willopenmenu%28_,with%29.md)
  Called just before a contextual menu for a view is opened on screen.
- [func didCloseMenu(NSMenu, with: NSEvent?)](./didclosemenu%28_,with%29.md)
  Called after a contextual menu that was displayed from the receiving view has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/defaultmenu)*