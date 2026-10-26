# cursorGlyphHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

A handler that the framework calls to change the cursor’s appearance.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) PGDisplayCursorGlyphHandler cursorGlyphHandler;
```

## See Also

### Managing Cursor Events
- [var cursorShowHandler: PGDisplayCursorShowHandler?](./cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [PGDisplayCursorGlyphHandler](../pgdisplaycursorglyphhandler.md)
  The block signature for a routine that handles changes to the cursor’s appearance.
- [typealias PGDisplayCursorShowHandler](../pgdisplaycursorshowhandler.md)
  The block signature for a routine that handles changes to the cursor’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/cursorglyphhandler)*