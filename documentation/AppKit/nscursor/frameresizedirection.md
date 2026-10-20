# NSCursor.FrameResizeDirection

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The direction in which a rectangular frame can be resized.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
enum FrameResizeDirection
```

## Topics

### Structures
- [NSCursor.FrameResizeDirection.Set](./frameresizedirection/set.md)
  An efficient set of frame resize directions.
### Enumeration Cases
- [NSCursor.FrameResizeDirection.inward](./frameresizedirection/inward.md)
  Indicates that the rectangular frame can be resized inwards to be smaller.
- [NSCursor.FrameResizeDirection.outward](./frameresizedirection/outward.md)
  Indicates that the rectangular frame can be resized outwards to be larger.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizedirection)*