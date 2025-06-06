# defaultMenu

**Framework**: AppKit  
**Kind**: property

Returns the default menu for instances of the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var defaultMenu: NSMenu? { get }
```

#### Return Value

The default menu. The `NSCell` implementation of this method returns `nil`.

## See Also

- [var menu: NSMenu?](nscell/menu.md)
  The cell’s contextual menu.
- [func menu(for: NSEvent, in: NSRect, of: NSView) -> NSMenu?](nscell/menu(for:in:of:).md)
  Returns the menu associated with the cell and related to the specified event and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/defaultmenu)*