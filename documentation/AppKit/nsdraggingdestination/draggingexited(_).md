# draggingExited(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func draggingExited(_ sender: (any NSDraggingInfo)?)
```

```objc
- (void) draggingExited:(id<NSDraggingInfo>) sender;
```

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

### Managing a Dragging Session Before an Image Is Released
- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](./draggingentered%28_%29.md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func wantsPeriodicDraggingUpdates() -> Bool](./wantsperiodicdraggingupdates%28%29.md)
  Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](./draggingupdated%28_%29.md) messages.
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](./draggingupdated%28_%29.md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingEnded(any NSDraggingInfo)](./draggingended%28_%29.md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/draggingexited(_:))*