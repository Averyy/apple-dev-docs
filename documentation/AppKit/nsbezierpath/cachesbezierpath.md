# cachesBezierPath

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether this object maintains a cached image of its path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

## Declaration

```objc
- (BOOL) cachesBezierPath;
```

## Return Value

[`true`](../../Swift/true.md) if the path maintains a cached image; otherwise, [`false`](../../Swift/false.md).

## Discussion

Caching of paths currently has no effect, so method always returns NO.

## See Also

### Deprecated
- [func appendGlyph(NSGlyph, in: NSFont)](./appendglyph%28_,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](./appendglyphs%28_,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](./appendpackedglyphs%28_%29.md)
  Appends an array of packed glyphs to the path.
- [- setCachesBezierPath:](./setcachesbezierpath_.md)
  Sets whether the path should cache its path information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/cachesbezierpath)*