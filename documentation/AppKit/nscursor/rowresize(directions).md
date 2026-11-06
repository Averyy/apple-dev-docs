# rowResize(directions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the cursor for resizing a row (horizontal divider) in the specified directions.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class func rowResize(directions: NSVerticalDirection.Set) -> NSCursor
```

## Return Value

The row-resize cursor for the specified directions.

## Discussion

The cursor shows the directions in which the row can resize. The following table shows the cursor for each set of directions:

| Directions | Cursor |
| --- | --- |
| `.up` | ![row-resize cursor, up](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-up@2x.png) |
| `.down` | ![row-resize cursor, down](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-down@2x.png) |
| `.all` | ![row-resize cursor, up and down](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-resize-up-down@2x.png) |

## Parameters

- `directions`: The direction in which a row can resize. This must not be empty.

## See Also

### Retrieving cursor instances
- [class var current: NSCursor](./current.md)
  Returns the application’s current cursor.
- [class var arrow: NSCursor](./arrow.md)
  Returns the default cursor, the arrow cursor.
- [class var contextualMenu: NSCursor](./contextualmenu.md)
  Returns the contextual menu system cursor.
- [class var closedHand: NSCursor](./closedhand.md)
  Returns the closed-hand system cursor.
- [class var crosshair: NSCursor](./crosshair.md)
  Returns the cross-hair system cursor.
- [class var disappearingItem: NSCursor](./disappearingitem.md)
  Returns a cursor indicating that the current operation will result in a disappearing item.
- [class var dragCopy: NSCursor](./dragcopy.md)
  Returns a cursor indicating that the current operation will result in a copy action.
- [class var dragLink: NSCursor](./draglink.md)
  Returns a cursor indicating that the current operation will result in a link action.
- [class var iBeam: NSCursor](./ibeam.md)
  Returns a cursor that looks like a capital I with a tiny crossbeam at its middle.
- [class var iBeamCursorForVerticalLayout: NSCursor](./ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
- [class var openHand: NSCursor](./openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](./operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](./pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var zoomIn: NSCursor](./zoomin.md)
  Returns the zoom-in cursor.
- [class var zoomOut: NSCursor](./zoomout.md)
  Returns the zoom-out cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/rowresize(directions:))*