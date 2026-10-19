# appendPackedGlyphs(_:)

**Framework**: AppKit  
**Kind**: method

Appends an array of packed glyphs to the path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func appendPackedGlyphs(_ packedGlyphs: UnsafePointer<CChar>)
```

#### Discussion

You should avoid using this method directly. Instead, use the [`appendGlyph(_:in:)`](nsbezierpath/appendglyph(_:in:).md) and [`appendGlyphs(_:count:in:)`](nsbezierpath/appendglyphs(_:count:in:).md) methods to append glyphs to a path.

## Parameters

- `packedGlyphs`: A C-style array containing one or more `CGGlyph` data types terminated by a `NULL` character.

## See Also

- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
- [func appendGlyph(NSGlyph, in: NSFont)](nsbezierpath/appendglyph(_:in:).md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](nsbezierpath/appendglyphs(_:count:in:).md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendpackedglyphs(_:))*