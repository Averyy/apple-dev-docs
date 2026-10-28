# trackMouse(with:adding:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles user manipulation of the receiver in its ruler view.

**Availability**:
- macOS

## Declaration

```swift
func trackMouse(with mouseDownEvent: NSEvent, adding isAdding: Bool) -> Bool
```

```objc
- (BOOL) trackMouse:(NSEvent *) mouseDownEvent adding:(BOOL) isAdding;
```

## Return Value

[`true`](../../Swift/true.md) if the user manipulation was allowed, [`false`](../../Swift/false.md) if it was not allowed.

## Discussion

[`NSRulerView`](../nsrulerview.md) objects invoke this method automatically to add a new marker or to move or remove an existing marker. You should never need to invoke it directly.

If the receiver is a new marker being added to its ruler view (`flag` is [`true`](../../Swift/true.md)), the receiver queries the ruler view’s client before adding itself to the ruler view. If the client responds to [`rulerView(_:shouldAdd:)`](../nsview/rulerview%28_,shouldadd%29.md) and that method returns [`false`](../../Swift/false.md), this method immediately returns [`false`](../../Swift/false.md), and the new marker isn’t added.

If the receiver is not a new marker being added to its ruler view (`flag` is [`false`](../../Swift/false.md)), this method attempts to move or remove an existing marker, once again based on responses from the ruler view’s client view. If the receiver is neither movable nor removable, this method immediately returns [`false`](../../Swift/false.md). Further, if the ruler view’s client responds to [`rulerView(_:shouldMove:)`](../nsview/rulerview%28_,shouldmove%29.md) and returns [`false`](../../Swift/false.md), this method returns [`false`](../../Swift/false.md), indicating the receiver can’t be moved.

If the receiver is being added or moved, this method queries the client view using [`rulerView(_:willAdd:atLocation:)`](../nsview/rulerview%28_,willadd,atlocation%29.md) or [`rulerView(_:willMove:toLocation:)`](../nsview/rulerview%28_,willmove,tolocation%29.md), respectively. If the client responds to the method, the return value is used as the receiver’s location. These methods are invoked repeatedly as the receiver is dragged within the ruler view.

If the receiver is an existing marker being removed (dragged off the ruler), this method queries the client view using [`rulerView(_:shouldRemove:)`](../nsview/rulerview%28_,shouldremove%29.md). If the client responds to this method and returns [`false`](../../Swift/false.md), the marker is pinned to the ruler view’s baseline (following the cursor on the baseline if it’s movable).

When the user releases the mouse button, this method informs the client view of the marker’s new status using [`rulerView(_:didAdd:)`](../nsview/rulerview%28_,didadd%29.md), [`rulerView(_:didMove:)`](../nsview/rulerview%28_,didmove%29.md), or [`rulerView(_:didRemove:)`](../nsview/rulerview%28_,didremove%29.md) as appropriate. The client view can use this notification to set the marker’s represented object, modify its state and redisplay (for example, adjusting text layout around a new tab stop), or take whatever other action it might need.

If `flag` is [`true`](../../Swift/true.md) and the user dragged the new marker away from the ruler, the marker isn’t added, no message is sent, and this method returns [`false`](../../Swift/false.md).

See [Ruler and Paragraph Style Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Rulers.html#//apple_ref/doc/uid/10000089i) for more information on these client methods.

## Parameters

- `mouseDownEvent`: The event that represents the user manipulation being attempted on the ruler marker.
- `isAdding`: [`true`](../../Swift/true.md) to indicate that the receiver is a new marker being added to its ruler view, [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [var isMovable: Bool](./ismovable.md)
  A Boolean that indicates whether the user can move the receiver in its ruler view.
- [var isRemovable: Bool](./isremovable.md)
  A Boolean that indicates whether the user can remove the receiver from its ruler view.
### Drawing and event handling
- [func draw(NSRect)](./draw%28_%29.md)
  Draws the receiver’s image that appears in the supplied rectangle.
- [var isDragging: Bool](./isdragging.md)
  A Boolean that indicates whether the receiver is being dragged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/trackmouse(with:adding:))*