# crosshair

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the cross-hair system cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class var crosshair: NSCursor { get }
```

```objc
@property (class, strong, readonly) NSCursor * crosshairCursor;
```

## Return Value

The cross-hair cursor. This cursor is used for situations when precise location is required (where the lines cross is the hot spot).

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
- [class var columnResize: NSCursor](./columnresize.md)
  Returns the cursor for resizing a column (vertical divider) in either direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/crosshair)*