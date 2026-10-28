# setCachesBezierPath:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the path should cache its path information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

## Declaration

```objc
- (void) setCachesBezierPath:(BOOL) flag;
```

## Discussion

Caching of paths currently has no effect.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the receiver should cache its path information; otherwise, [`false`](../../Swift/false.md).

## See Also

### Deprecated
- [func appendGlyph(NSGlyph, in: NSFont)](./appendglyph%28_,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](./appendglyphs%28_,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](./appendpackedglyphs%28_%29.md)
  Appends an array of packed glyphs to the path.
- [- cachesBezierPath](./cachesbezierpath.md)
  Returns a Boolean value that indicates whether this object maintains a cached image of its path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/setcachesbezierpath:)*