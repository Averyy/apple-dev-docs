# removeCursorRect(_:cursor:)

**Framework**: AppKit  
**Kind**: method

Completely removes a cursor rectangle from the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeCursorRect(_ rect: NSRect, cursor object: NSCursor)
```

#### Discussion

You should rarely need to use this method. The [`resetCursorRects()`](nsview/resetcursorrects().md) method, which is called when the cursor rectangles need to be rebuilt, should establish only the cursor rectangles needed. If you implement [`resetCursorRects()`](nsview/resetcursorrects().md) in this way, you can then simply modify the state that [`resetCursorRects()`](nsview/resetcursorrects().md) uses to build its cursor rectangles and then invoke the `NSWindow` method [`invalidateCursorRects(for:)`](nswindow/invalidatecursorrects(for:).md).

## Parameters

- `rect`: A rectangle defining a region of the view. Must match a value previously specified using  .
- `object`: An object representing a cursor. Must match a value previously specified using  .

## See Also

- [func addCursorRect(NSRect, cursor: NSCursor)](nsview/addcursorrect(_:cursor:).md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func discardCursorRects()](nsview/discardcursorrects.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md).
- [func resetCursorRects()](nsview/resetcursorrects.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removecursorrect(_:cursor:))*