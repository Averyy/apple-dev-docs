# PGDisplayCursorShowHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that handles changes to the cursor’s visibility.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDisplayCursorShowHandler = (Bool) -> Void
```

## Parameters

- `show`: A Boolean value that indicates whether to show the cursor.

## See Also

- [var cursorGlyphHandler: PGDisplayCursorGlyphHandler?](pgdisplaydescriptor/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](pgdisplaydescriptor/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [typealias PGDisplayCursorGlyphHandler](pgdisplaycursorglyphhandler.md)
  The block signature for a routine that handles changes to the cursor’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaycursorshowhandler)*