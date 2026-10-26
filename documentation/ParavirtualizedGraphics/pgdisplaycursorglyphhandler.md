# PGDisplayCursorGlyphHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that handles changes to the cursor’s appearance.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef void (^)(NSBitmapImageRep *, PGDisplayCoord_t) PGDisplayCursorGlyphHandler;
```

## Parameters

- `glyph`: The image to assign to the cursor.
- `hotSpot   `: The point to set as the cursor’s hot spot.

## See Also

### Managing Cursor Events
- [cursorGlyphHandler](./pgdisplaydescriptor/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](./pgdisplaydescriptor/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [typealias PGDisplayCursorShowHandler](./pgdisplaycursorshowhandler.md)
  The block signature for a routine that handles changes to the cursor’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaycursorglyphhandler)*