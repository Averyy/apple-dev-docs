# appendPackedGlyphs(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends an array of packed glyphs to the path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`append(withCGGlyphs:count:in:)`](./append%28withcgglyphs,count,in%29.md) instead.

## Declaration

```swift
func appendPackedGlyphs(_ packedGlyphs: UnsafePointer<CChar>)
```

```objc
- (void) appendBezierPathWithPackedGlyphs:(const char *) packedGlyphs;
```

#### Discussion

You should avoid using this method directly. Instead, use the [`appendGlyph(_:in:)`](./appendglyph%28_,in%29.md) and [`appendGlyphs(_:count:in:)`](./appendglyphs%28_,count,in%29.md) methods to append glyphs to a path.

## Parameters

- `packedGlyphs`: A C-style array containing one or more `CGGlyph` data types terminated by a `NULL` character.

## See Also

### Related Documentation
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
### Deprecated
- [func appendGlyph(NSGlyph, in: NSFont)](./appendglyph%28_,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](./appendglyphs%28_,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.
- [- cachesBezierPath](./cachesbezierpath.md)
  Returns a Boolean value that indicates whether this object maintains a cached image of its path.
- [- setCachesBezierPath:](./setcachesbezierpath_.md)
  Sets whether the path should cache its path information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendpackedglyphs(_:))*