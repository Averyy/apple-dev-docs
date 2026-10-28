# getBoundingRects(_:forCGGlyphs:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func getBoundingRects(_ bounds: NSRectArray, forCGGlyphs glyphs: UnsafePointer<CGGlyph>, count glyphCount: Int)
```

```objc
- (void) getBoundingRects:(NSRectArray) bounds forCGGlyphs:(const CGGlyph *) glyphs count:(NSUInteger) glyphCount;
```

## Discussion

Returns in `bounds` an array of the bounding rectangles for the glyphs specified by `glyphs` and rendered by the receiver. The `glyphCount` value must specify the count of glyphs passed in `glyphs`.

## See Also

### Getting Bounding Rectangles
- [var boundingRectForFont: NSRect](./boundingrectforfont.md)
  The font’s bounding rectangle, scaled to the font’s size.
- [func boundingRect(forCGGlyph: CGGlyph) -> NSRect](./boundingrect%28forcgglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/getboundingrects(_:forcgglyphs:count:))*