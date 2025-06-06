# draggingExited(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func draggingExited(_ sender: (any NSDraggingInfo)?)
```

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingentered(_:).md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func wantsPeriodicDraggingUpdates() -> Bool](nsdraggingdestination/wantsperiodicdraggingupdates.md)
  Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages.
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingupdated(_:).md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingEnded(any NSDraggingInfo)](nsdraggingdestination/draggingended(_:).md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/draggingexited(_:))*