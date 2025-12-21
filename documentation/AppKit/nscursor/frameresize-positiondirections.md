# frameResize(position:directions:)

**Framework**: AppKit  
**Kind**: method

Returns the cursor for resizing a rectangular frame from the specified edge or corner.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class func frameResize(position: NSCursor.FrameResizePosition, directions: NSCursor.FrameResizeDirection.Set) -> NSCursor
```

## Parameters

- `position`: The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- `directions`: The directions in which a rectangular frame can be resized. This must not be empty.

## See Also

- [class var current: NSCursor](nscursor/current.md)
  Returns the application’s current cursor.
- [class var currentSystem: NSCursor?](nscursor/currentsystem.md)
  Returns the current system cursor.
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
- [class var iBeamCursorForVerticalLayout: NSCursor](nscursor/ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
- [class var openHand: NSCursor](nscursor/openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](nscursor/operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](nscursor/pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var zoomIn: NSCursor](nscursor/zoomin.md)
  Returns the zoom-in cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresize(position:directions:))*