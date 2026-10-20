# menu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s contextual menu.

**Availability**:
- macOS

## Declaration

```swift
var menu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * menu;
```

#### Discussion

Use this property to specify a menu containing contextual commands associated with the cell. If the cell does not have a menu, set this property to `nil`.

## See Also

### Managing Menus
- [class var defaultMenu: NSMenu?](./defaultmenu.md)
  Returns the default menu for instances of the cell.
- [func menu(for: NSEvent, in: NSRect, of: NSView) -> NSMenu?](./menu%28for,in,of%29.md)
  Returns the menu associated with the cell and related to the specified event and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/menu)*