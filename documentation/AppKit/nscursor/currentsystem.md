# currentSystem

**Framework**: AppKit  
**Kind**: property

Returns the current system cursor.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
class var currentSystem: NSCursor? { get }
```

#### Return Value

A cursor whose image and hot spot match those of the currently-displayed cursor on the system

#### Discussion

This method returns the current system cursor regardless of which application set the cursor, and whether Cocoa or Carbon APIs were used to set it.

This method replaces the now deprecated QDGetCursorData function.

## See Also

- [class var resizeDown: NSCursor](nscursor/resizedown.md)
  Returns the resize-down system cursor.
- [class var resizeLeft: NSCursor](nscursor/resizeleft.md)
  Returns the resize-left system cursor.
- [class var resizeLeftRight: NSCursor](nscursor/resizeleftright.md)
  Returns the resize-left-and-right system cursor.
- [class var resizeRight: NSCursor](nscursor/resizeright.md)
  Returns the resize-right system cursor.
- [class var resizeUp: NSCursor](nscursor/resizeup.md)
  Returns the resize-up system cursor.
- [class var resizeUpDown: NSCursor](nscursor/resizeupdown.md)
  Returns the resize-up-and-down system cursor.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/currentsystem)*