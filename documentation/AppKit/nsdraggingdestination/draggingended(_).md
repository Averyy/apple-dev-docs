# draggingEnded(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called when a drag operation ends.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func draggingEnded(_ sender: any NSDraggingInfo)
```

```objc
- (void) draggingEnded:(id<NSDraggingInfo>) sender;
```

#### Discussion

Implement this method if you want to be notified when a drag operation ends, which can be useful if the drag ends in some other destination. For example, this method might be used by a destination doing auto-expansion in order to collapse any auto-expands.

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
- [func draggingExited((any NSDraggingInfo)?)](./draggingexited%28_%29.md)
  Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/draggingended(_:))*