# trackMouse(with:adding:)

**Framework**: AppKit  
**Kind**: method

Handles user manipulation of the receiver in its ruler view.

**Availability**:
- macOS ?+

## Declaration

```swift
func trackMouse(with mouseDownEvent: NSEvent, adding isAdding: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the user manipulation was allowed, [`false`](https://developer.apple.com/documentation/Swift/false) if it was not allowed.

#### Discussion

[`NSRulerView`](nsrulerview.md) objects invoke this method automatically to add a new marker or to move or remove an existing marker. You should never need to invoke it directly.

If the receiver is a new marker being added to its ruler view (`flag` is [`true`](https://developer.apple.com/documentation/Swift/true)), the receiver queries the ruler view’s client before adding itself to the ruler view. If the client responds to [`rulerView(_:shouldAdd:)`](nsview/rulerview(_:shouldadd:).md) and that method returns [`false`](https://developer.apple.com/documentation/Swift/false), this method immediately returns [`false`](https://developer.apple.com/documentation/Swift/false), and the new marker isn’t added.

If the receiver is not a new marker being added to its ruler view (`flag` is [`false`](https://developer.apple.com/documentation/Swift/false)), this method attempts to move or remove an existing marker, once again based on responses from the ruler view’s client view. If the receiver is neither movable nor removable, this method immediately returns [`false`](https://developer.apple.com/documentation/Swift/false). Further, if the ruler view’s client responds to [`rulerView(_:shouldMove:)`](nsview/rulerview(_:shouldmove:).md) and returns [`false`](https://developer.apple.com/documentation/Swift/false), this method returns [`false`](https://developer.apple.com/documentation/Swift/false), indicating the receiver can’t be moved.

If the receiver is being added or moved, this method queries the client view using [`rulerView(_:willAdd:atLocation:)`](nsview/rulerview(_:willadd:atlocation:).md) or [`rulerView(_:willMove:toLocation:)`](nsview/rulerview(_:willmove:tolocation:).md), respectively. If the client responds to the method, the return value is used as the receiver’s location. These methods are invoked repeatedly as the receiver is dragged within the ruler view.

If the receiver is an existing marker being removed (dragged off the ruler), this method queries the client view using [`rulerView(_:shouldRemove:)`](nsview/rulerview(_:shouldremove:).md). If the client responds to this method and returns [`false`](https://developer.apple.com/documentation/Swift/false), the marker is pinned to the ruler view’s baseline (following the cursor on the baseline if it’s movable).

When the user releases the mouse button, this method informs the client view of the marker’s new status using [`rulerView(_:didAdd:)`](nsview/rulerview(_:didadd:).md), [`rulerView(_:didMove:)`](nsview/rulerview(_:didmove:).md), or [`rulerView(_:didRemove:)`](nsview/rulerview(_:didremove:).md) as appropriate. The client view can use this notification to set the marker’s represented object, modify its state and redisplay (for example, adjusting text layout around a new tab stop), or take whatever other action it might need.

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true) and the user dragged the new marker away from the ruler, the marker isn’t added, no message is sent, and this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

See [`Ruler and Paragraph Style Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Rulers.html#//apple_ref/doc/uid/10000089i) for more information on these client methods.

## Parameters

- `mouseDownEvent`: The event that represents the user manipulation being attempted on the ruler marker.
- `isAdding`:   to indicate that the receiver is a new marker being added to its ruler view,   otherwise.

## See Also

- [var isMovable: Bool](nsrulermarker/ismovable.md)
  A Boolean that indicates whether the user can move the receiver in its ruler view.
- [var isRemovable: Bool](nsrulermarker/isremovable.md)
  A Boolean that indicates whether the user can remove the receiver from its ruler view.
- [func draw(NSRect)](nsrulermarker/draw(_:).md)
  Draws the receiver’s image that appears in the supplied rectangle.
- [var isDragging: Bool](nsrulermarker/isdragging.md)
  A Boolean that indicates whether the receiver is being dragged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/trackmouse(with:adding:))*