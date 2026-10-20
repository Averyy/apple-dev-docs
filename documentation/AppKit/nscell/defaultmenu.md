# defaultMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default menu for instances of the cell.

**Availability**:
- macOS

## Declaration

```swift
class var defaultMenu: NSMenu? { get }
```

```objc
@property (class, strong, readonly, nullable) NSMenu * defaultMenu;
```

#### Return Value

The default menu. The `NSCell` implementation of this method returns `nil`.

## See Also

### Managing Menus
- [var menu: NSMenu?](./menu.md)
  The cell’s contextual menu.
- [func menu(for: NSEvent, in: NSRect, of: NSView) -> NSMenu?](./menu%28for,in,of%29.md)
  Returns the menu associated with the cell and related to the specified event and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/defaultmenu)*