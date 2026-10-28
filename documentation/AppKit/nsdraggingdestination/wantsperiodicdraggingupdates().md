# wantsPeriodicDraggingUpdates()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](./draggingupdated%28_%29.md) messages.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func wantsPeriodicDraggingUpdates() -> Bool
```

```objc
- (BOOL) wantsPeriodicDraggingUpdates;
```

## Return Value

[`true`](../../Swift/true.md) if the destination wants to receive periodic [`draggingUpdated(_:)`](./draggingupdated%28_%29.md) messages, [`false`](../../Swift/false.md) otherwise.

## Discussion

If the destination returns [`false`](../../Swift/false.md), these messages are sent only when the mouse moves or a modifier flag changes. Otherwise the destination gets the default behavior, where it receives periodic dragging-updated messages even if nothing changes.

## See Also

### Managing a Dragging Session Before an Image Is Released
- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](./draggingentered%28_%29.md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](./draggingupdated%28_%29.md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingExited((any NSDraggingInfo)?)](./draggingexited%28_%29.md)
  Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).
- [func draggingEnded(any NSDraggingInfo)](./draggingended%28_%29.md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/wantsperiodicdraggingupdates())*