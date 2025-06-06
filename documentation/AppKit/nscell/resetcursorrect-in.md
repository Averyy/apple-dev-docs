# resetCursorRect(_:in:)

**Framework**: AppKit  
**Kind**: method

Sets the receiver to show the I-beam cursor while it tracks the mouse.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetCursorRect(_ cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

The receiver must be an enabled and selectable (or editable) text-type cell.

This method is invoked by [`resetCursorRects()`](nsview/resetcursorrects().md) and in general you do not need to call this method unless you have a custom `NSView` that uses a cell.

## Parameters

- `cellFrame`: The rectangle in which to display the I-beam cursor.
- `controlView`: The control that manages the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/resetcursorrect(_:in:))*