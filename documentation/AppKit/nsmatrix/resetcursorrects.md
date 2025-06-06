# resetCursorRects()

**Framework**: AppKit  
**Kind**: method

Resets cursor rectangles so the cursor becomes an I-beam over text cells.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetCursorRects()
```

#### Discussion

This method resets the cursor rectangles by sending [`resetCursorRect(_:in:)`](nscell/resetcursorrect(_:in:).md) to each cell in the receiver. Any cell that has a cursor rectangle to set up should then send [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md) back to the receiver.

## See Also

- [func addCursorRect(NSRect, cursor: NSCursor)](nsview/addcursorrect(_:cursor:).md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func resetCursorRect(NSRect, in: NSView)](nscell/resetcursorrect(_:in:).md)
  Sets the receiver to show the I-beam cursor while it tracks the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/resetcursorrects())*