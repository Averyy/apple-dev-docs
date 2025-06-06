# textTab(forGlyphLocation:writingDirection:maxLocation:)

**Framework**: AppKit  
**Kind**: method

Returns the text tab next closest to a given glyph location within the given parameters.

**Availability**:
- macOS ?+

## Declaration

```swift
func textTab(forGlyphLocation glyphLocation: CGFloat, writingDirection direction: NSWritingDirection, maxLocation: CGFloat) -> NSTextTab?
```

#### Return Value

The text tab next closest to `glyphLocation`, indexing in `direction` but not beyond `maxLocation`.

#### Discussion

The typesetter calls this method whenever it finds a tab character. To determine the width to advance the next glyph, the typesetter examines the [`NSParagraphStyle`](nsparagraphstyle.md) object’s tab array and the default tab interval.

## Parameters

- `glyphLocation`: The location at which to start searching.
- `direction`: The direction in which to search.
- `maxLocation`: The maximum location for the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/texttab(forglyphlocation:writingdirection:maxlocation:))*