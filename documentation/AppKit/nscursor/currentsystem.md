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

- [class var current: NSCursor](nscursor/current.md)
  Returns the application’s current cursor.
- [class var arrow: NSCursor](nscursor/arrow.md)
  Returns the default cursor, the arrow cursor.
- [class var contextualMenu: NSCursor](nscursor/contextualmenu.md)
  Returns the contextual menu system cursor.
- [class var closedHand: NSCursor](nscursor/closedhand.md)
  Returns the closed-hand system cursor.
- [class var crosshair: NSCursor](nscursor/crosshair.md)
  Returns the cross-hair system cursor.
- [class var disappearingItem: NSCursor](nscursor/disappearingitem.md)
  Returns a cursor indicating that the current operation will result in a disappearing item.
- [class var dragCopy: NSCursor](nscursor/dragcopy.md)
  Returns a cursor indicating that the current operation will result in a copy action.
- [class var dragLink: NSCursor](nscursor/draglink.md)
  Returns a cursor indicating that the current operation will result in a link action.
- [class var iBeam: NSCursor](nscursor/ibeam.md)
  Returns a cursor that looks like a capital I with a tiny crossbeam at its middle.
- [class var openHand: NSCursor](nscursor/openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](nscursor/operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](nscursor/pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var resizeDown: NSCursor](nscursor/resizedown.md)
  Returns the resize-down system cursor.
- [class var resizeLeft: NSCursor](nscursor/resizeleft.md)
  Returns the resize-left system cursor.
- [class var resizeLeftRight: NSCursor](nscursor/resizeleftright.md)
  Returns the resize-left-and-right system cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/currentsystem)*