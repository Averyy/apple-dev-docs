# resetCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resets cursor rectangles so the cursor becomes an I-beam over text cells.

**Availability**:
- macOS

## Declaration

```swift
func resetCursorRects()
```

```objc
- (void) resetCursorRects;
```

## Discussion

This method resets the cursor rectangles by sending [`resetCursorRect(_:in:)`](../nscell/resetcursorrect%28_,in%29.md) to each cell in the receiver. Any cell that has a cursor rectangle to set up should then send [`addCursorRect(_:cursor:)`](../nsview/addcursorrect%28_,cursor%29.md) back to the receiver.

## See Also

### Related Documentation
- [func addCursorRect(NSRect, cursor: NSCursor)](../nsview/addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func resetCursorRect(NSRect, in: NSView)](../nscell/resetcursorrect%28_,in%29.md)
  Sets the receiver to show the I-beam cursor while it tracks the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/resetcursorrects())*