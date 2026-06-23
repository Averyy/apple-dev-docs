# selectionManager(_:frameOfTextContainerAt:)

**Framework**: AppKit  
**Kind**: method

Returns the frame of the text container at the specified point.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func selectionManager(_ selectionManager: NSTextSelectionManager, frameOfTextContainerAt point: NSPoint) -> NSRect
```

#### Return Value

The frame of the text container at the point, in the view’s coordinate system, or `NSZeroRect` if no container exists there.

#### Discussion

Implement this method whenever your text container is not positioned at the view’s origin (0, 0), or whenever your view hosts multiple text containers. The selection manager uses the returned frame to convert gesture points from view coordinates into container-local coordinates before forwarding them to [`NSTextSelectionDataSource`](nstextselectiondatasource.md). Without this method the selection manager assumes the container fills the view starting at the origin, which produces incorrect points for any other layout.

For multi-container layouts, also implement `selectionManager:locationOfTextContainerAtPoint:` so the selection manager can identify which container a gesture targets.

## Parameters

- `selectionManager`: The selection manager requesting the frame.
- `point`: The point in the view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:frameoftextcontainerat:))*