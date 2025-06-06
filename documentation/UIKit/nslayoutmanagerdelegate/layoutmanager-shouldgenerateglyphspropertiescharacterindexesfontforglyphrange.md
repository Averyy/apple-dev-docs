# layoutManager(_:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:)

**Framework**: UIKit  
**Kind**: method

Enables customization of the initial glyph generation process.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange) -> Int
```

#### Return Value

The actual glyph range stored in this method. By returning `0`, it can indicate for the layout manager to do the default processing.

#### Discussion

This message is sent whenever the layout manager is about to store the initial glyph information via [`setGlyphs(_:properties:characterIndexes:font:forGlyphRange:)`](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md). To customize the initial glyph generation process, this method can invoke [`setGlyphs(_:properties:characterIndexes:font:forGlyphRange:)`](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md) with modified glyph information.

> **Note**:  Querying glyph information surrounding `glyphRange` could lead to recursion since the data might not be available yet.

 Querying glyph information surrounding `glyphRange` could lead to recursion since the data might not be available yet.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `glyphs`: A pointer to the layout manager’s glyph cache.
- `props`: A pointer to a buffer containing glyph properties for the glyphs in the cache.
- `charIndexes`: A pointer to the starting index for the characters in the text storage for which glyphs are generated.
- `aFont`: A font to override the font attributes in the text storage for the specified character range.
- `glyphRange`: The range of glyphs in the glyph cache to set.

## See Also

- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:).md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md)
  Returns the control character action for the control character at the specified character index.
- [NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:))*