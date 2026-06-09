# selectionManager(_:shouldBeginSelectionAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether a selection can begin at the specified point.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func selectionManager(_ selectionManager: NSTextSelectionManager, shouldBeginSelectionAt point: NSPoint) -> Bool
```

#### Return Value

`YES` if selection can begin at the point; otherwise, `NO`.

#### Discussion

Return `YES` to allow a text selection to begin at the specified point, `NO` to prevent it. If the delegate doesn’t implement this method, selection is always allowed. The selection manager calls this method when the user initiates a selection gesture at the given point in the coordinate system of the view containing the selection manager.

## Parameters

- `selectionManager`: The selection manager requesting permission.
- `point`: The point in the view’s coordinate system where the selection gesture began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:shouldbeginselectionat:))*