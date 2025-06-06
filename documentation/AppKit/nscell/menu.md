# menu

**Framework**: AppKit  
**Kind**: property

The cell’s contextual menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var menu: NSMenu? { get set }
```

#### Discussion

Use this property to specify a menu containing contextual commands associated with the cell. If the cell does not have a menu, set this property to `nil`.

## See Also

- [class var defaultMenu: NSMenu?](nscell/defaultmenu.md)
  Returns the default menu for instances of the cell.
- [func menu(for: NSEvent, in: NSRect, of: NSView) -> NSMenu?](nscell/menu(for:in:of:).md)
  Returns the menu associated with the cell and related to the specified event and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/menu)*