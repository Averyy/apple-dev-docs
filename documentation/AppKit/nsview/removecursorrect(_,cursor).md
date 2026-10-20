# removeCursorRect(_:cursor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Completely removes a cursor rectangle from the view.

**Availability**:
- macOS

## Declaration

```swift
func removeCursorRect(_ rect: NSRect, cursor object: NSCursor)
```

```objc
- (void) removeCursorRect:(NSRect) rect cursor:(NSCursor *) object;
```

#### Discussion

You should rarely need to use this method. The [`resetCursorRects()`](./resetcursorrects%28%29.md) method, which is called when the cursor rectangles need to be rebuilt, should establish only the cursor rectangles needed. If you implement [`resetCursorRects()`](./resetcursorrects%28%29.md) in this way, you can then simply modify the state that [`resetCursorRects()`](./resetcursorrects%28%29.md) uses to build its cursor rectangles and then invoke the `NSWindow` method [`invalidateCursorRects(for:)`](../nswindow/invalidatecursorrects%28for%29.md).

## Parameters

- `rect`: A rectangle defining a region of the view. Must match a value previously specified using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).
- `object`: An object representing a cursor. Must match a value previously specified using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).

## See Also

### Responding to Cursor Movements
- [func addCursorRect(NSRect, cursor: NSCursor)](./addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removecursorrect(_:cursor:))*