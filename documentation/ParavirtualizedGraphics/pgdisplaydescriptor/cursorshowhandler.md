# cursorShowHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property

A handler that the framework calls to change the cursor’s visibility.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var cursorShowHandler: PGDisplayCursorShowHandler? { get set }
```

## See Also

- [var cursorGlyphHandler: PGDisplayCursorGlyphHandler?](pgdisplaydescriptor/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [typealias PGDisplayCursorGlyphHandler](pgdisplaycursorglyphhandler.md)
  The block signature for a routine that handles changes to the cursor’s appearance.
- [typealias PGDisplayCursorShowHandler](pgdisplaycursorshowhandler.md)
  The block signature for a routine that handles changes to the cursor’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/cursorshowhandler)*