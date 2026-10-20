# screenFont(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.

**Availability**:
- macOS

## Declaration

```swift
func screenFont(with renderingMode: NSFontRenderingMode) -> NSFont
```

```objc
- (NSFont *) screenFontWithRenderingMode:(NSFontRenderingMode) renderingMode;
```

#### Discussion

For valid rendering modes, see [`NSFontRenderingMode`](../nsfontrenderingmode.md).

Screen fonts are for direct use with the window server only. Never use them with Application Kit objects, such as in `setFont:` methods. Internally, the Application Kit automatically uses the corresponding screen font for a font object as long as the view is not rotated or scaled.

## See Also

### Related Documentation
- [var screen: NSFont](./screen.md)
  The bitmapped screen font for the current font.
- [var printer: NSFont](./printer.md)
  The scalable PostScript font corresponding to current font.
### Instance Methods
- [func advancement(forGlyph: NSGlyph) -> NSSize](./advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getadvancements%28_,forglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](./getadvancements%28_,forpackedglyphs,length%29.md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getboundingrects%28_,forglyphs,count%29.md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](./glyph%28withname%29.md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func withSize(CGFloat) -> NSFont](./withsize%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/screenfont(with:))*