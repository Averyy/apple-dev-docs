# PGDisplayCursorGlyphHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that handles changes to the cursor’s appearance.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDisplayCursorGlyphHandler = (NSBitmapImageRep, PGDisplayCoord_t) -> Void
```

## Parameters

- `glyph`: The image to assign to the cursor.
- `hotSpot   `: The point to set as the cursor’s hot spot.

## See Also

- [var cursorGlyphHandler: PGDisplayCursorGlyphHandler?](pgdisplaydescriptor/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](pgdisplaydescriptor/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [typealias PGDisplayCursorShowHandler](pgdisplaycursorshowhandler.md)
  The block signature for a routine that handles changes to the cursor’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaycursorglyphhandler)*