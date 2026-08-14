# wantsPeriodicDraggingUpdates()

**Framework**: AppKit  
**Kind**: method

Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func wantsPeriodicDraggingUpdates() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the destination wants to receive periodic [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

If the destination returns [`false`](https://developer.apple.com/documentation/swift/false), these messages are sent only when the mouse moves or a modifier flag changes. Otherwise the destination gets the default behavior, where it receives periodic dragging-updated messages even if nothing changes.

## See Also

- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingentered(_:).md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingupdated(_:).md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingExited((any NSDraggingInfo)?)](nsdraggingdestination/draggingexited(_:).md)
  Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).
- [func draggingEnded(any NSDraggingInfo)](nsdraggingdestination/draggingended(_:).md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/wantsperiodicdraggingupdates())*