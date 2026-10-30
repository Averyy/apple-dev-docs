# menu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the responder’s menu.

**Availability**:
- macOS

## Declaration

```swift
var menu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * menu;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

For `NSApplication` this menu is the same as the menu returned by its [`mainMenu`](../nsapplication/mainmenu.md) property.

## See Also

### Related Documentation
- [class var defaultMenu: NSMenu?](../nsview/defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func menu(for: NSEvent) -> NSMenu?](../nsview/menu%28for%29.md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/menu)*