# selectionManager(_:locationOfTextContainerAt:)

**Framework**: AppKit  
**Kind**: method

Returns the text location of the text container at the specified point.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func selectionManager(_ selectionManager: NSTextSelectionManager, locationOfTextContainerAt point: NSPoint) -> (any NSTextLocation)?
```

#### Return Value

The text location for the text container at the point, or `nil` if no container exists there.

#### Discussion

Implement this method to support layouts with multiple text containers, such as multi-column or paginated layouts. For full multiple-text-container support, also implement `selectionManager:frameOfTextContainerAtPoint:`.

## Parameters

- `selectionManager`: The selection manager requesting the text location.
- `point`: The point in the view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:locationoftextcontainerat:))*