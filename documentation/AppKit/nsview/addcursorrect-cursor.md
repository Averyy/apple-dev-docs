# addCursorRect(_:cursor:)

**Framework**: AppKit  
**Kind**: method

Establishes  the cursor to be used when the mouse pointer lies within a specified region.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addCursorRect(_ rect: NSRect, cursor object: NSCursor)
```

#### Discussion

Cursor rectangles aren’t subject to clipping by superviews, nor are they intended for use with rotated views. You should explicitly confine a cursor rectangle to the view’s visible rectangle to prevent improper behavior.

This method is intended to be invoked only by the [`resetCursorRects()`](nsview/resetcursorrects().md) method. If invoked in any other way, the resulting cursor rectangle will be discarded the next time the view’s cursor rectangles are rebuilt.

## Parameters

- `rect`: A rectangle defining a region of the view.
- `object`: An object representing a cursor.

## See Also

- [var visibleRect: NSRect](nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func removeCursorRect(NSRect, cursor: NSCursor)](nsview/removecursorrect(_:cursor:).md)
  Completely removes a cursor rectangle from the view.
- [func discardCursorRects()](nsview/discardcursorrects.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md).
- [func resetCursorRects()](nsview/resetcursorrects.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addcursorrect(_:cursor:))*