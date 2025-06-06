# textTab(forGlyphLocation:writingDirection:maxLocation:)

**Framework**: AppKit  
**Kind**: method

Returns the text tab closest to the specified glyph location and not beyond a maximum position.

**Availability**:
- macOS ?+

## Declaration

```swift
func textTab(forGlyphLocation glyphLocation: CGFloat, writingDirection direction: NSWritingDirection, maxLocation: CGFloat) -> NSTextTab?
```

#### Discussion

The typesetter calls this method whenever it finds a tab character. To determine the width to advance the next glyph, the typesetter examines the [`NSParagraphStyle`](nsparagraphstyle.md) tab array and the default tab interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/texttab(forglyphlocation:writingdirection:maxlocation:))*