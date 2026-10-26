# frameResizeCursorFromPosition:inDirections:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the cursor for resizing a rectangular frame from the specified edge or corner.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```objc
+ (NSCursor *) frameResizeCursorFromPosition:(NSCursorFrameResizePosition) position inDirections:(NSCursorFrameResizeDirections) directions;
```

## Parameters

- `position`: The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- `directions`: The directions in which a rectangular frame can be resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizecursorfromposition:indirections:)*