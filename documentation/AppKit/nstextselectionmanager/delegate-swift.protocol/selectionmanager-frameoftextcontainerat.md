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

The frame of the text container at the point, in the text container’s coordinate system, or `NSZeroRect` if no container exists there.

#### Discussion

Implement this method to support layouts with multiple text containers. For full multiple-text-container support, also implement `selectionManager:locationOfTextContainerAtPoint:`.

## Parameters

- `selectionManager`: The selection manager requesting the frame.
- `point`: The point in the view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:frameoftextcontainerat:))*