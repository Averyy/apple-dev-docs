# boundingRectForFont

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font’s bounding rectangle, scaled to the font’s size.

**Availability**:
- macOS

## Declaration

```swift
var boundingRectForFont: NSRect { get }
```

```objc
@property (readonly) NSRect boundingRectForFont;
```

## Discussion

The bounding rectangle is the union of the bounding rectangles of every glyph in the font.

## See Also

### Related Documentation
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
### Getting Bounding Rectangles
- [func boundingRect(forCGGlyph: CGGlyph) -> NSRect](./boundingrect%28forcgglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getBoundingRects(NSRectArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](./getboundingrects%28_,forcgglyphs,count%29.md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/boundingrectforfont)*