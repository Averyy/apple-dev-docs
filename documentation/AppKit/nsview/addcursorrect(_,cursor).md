# addCursorRect(_:cursor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Establishes  the cursor to be used when the mouse pointer lies within a specified region.

**Availability**:
- macOS

## Declaration

```swift
func addCursorRect(_ rect: NSRect, cursor object: NSCursor)
```

```objc
- (void) addCursorRect:(NSRect) rect cursor:(NSCursor *) object;
```

#### Discussion

Cursor rectangles aren’t subject to clipping by superviews, nor are they intended for use with rotated views. You should explicitly confine a cursor rectangle to the view’s visible rectangle to prevent improper behavior.

This method is intended to be invoked only by the [`resetCursorRects()`](./resetcursorrects%28%29.md) method. If invoked in any other way, the resulting cursor rectangle will be discarded the next time the view’s cursor rectangles are rebuilt.

## Parameters

- `rect`: A rectangle defining a region of the view.
- `object`: An object representing a cursor.

## See Also

### Related Documentation
- [var visibleRect: NSRect](./visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
### Responding to Cursor Movements
- [func removeCursorRect(NSRect, cursor: NSCursor)](./removecursorrect%28_,cursor%29.md)
  Completely removes a cursor rectangle from the view.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addcursorrect(_:cursor:))*