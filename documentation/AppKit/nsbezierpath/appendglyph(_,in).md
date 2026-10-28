# appendGlyph(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends an outline of the specified glyph to the path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`append(withCGGlyph:in:)`](./append%28withcgglyph,in%29.md) instead.

## Declaration

```swift
func appendGlyph(_ glyph: NSGlyph, in font: NSFont)
```

```objc
- (void) appendBezierPathWithGlyph:(NSGlyph) glyph inFont:(NSFont *) font;
```

## Discussion

If the glyph is not encoded in the font specified by the `fontObj` parameter—that is, the font does not have an entry for the specified glyph—then no path is appended to the receiver.

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](../../Foundation/nsexceptionname/genericexception.md) exception.

## Parameters

- `glyph`: The glyph to add to the path.
- `font`: The font in which the glyph is encoded.

## See Also

### Related Documentation
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
### Deprecated
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](./appendglyphs%28_,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](./appendpackedglyphs%28_%29.md)
  Appends an array of packed glyphs to the path.
- [- cachesBezierPath](./cachesbezierpath.md)
  Returns a Boolean value that indicates whether this object maintains a cached image of its path.
- [- setCachesBezierPath:](./setcachesbezierpath_.md)
  Sets whether the path should cache its path information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendglyph(_:in:))*