# CTRunGetGlyphsPtr(_:)

**Framework**: Core Text  
**Kind**: func

Returns a direct pointer for the glyph array stored in the run.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTRunGetGlyphsPtr(_ run: CTRun) -> UnsafePointer<CGGlyph>?
```

#### Return Value

A valid pointer to an array of [`CGGlyph`](https://developer.apple.com/documentation/CoreGraphics/CGGlyph) structures, or `NULL`.

#### Discussion

The glyph array will have a length equal to the value returned by [`CTRunGetGlyphCount(_:)`](ctrungetglyphcount(_:).md). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. If this function returns `NULL`, the caller must allocate its own buffer and call [`CTRunGetGlyphs(_:_:_:)`](ctrungetglyphs(_:_:_:).md) to fetch the glyphs.

## Parameters

- `run`: The run from which to return glyphs.

## See Also

- [func CTRunGetGlyphCount(CTRun) -> CFIndex](ctrungetglyphcount(_:).md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](ctrungetattributes(_:).md)
  Returns the attribute dictionary that was used to create the glyph run.
- [func CTRunGetStatus(CTRun) -> CTRunStatus](ctrungetstatus(_:).md)
  Returns the run’s status.
- [func CTRunGetGlyphs(CTRun, CFRange, UnsafeMutablePointer<CGGlyph>)](ctrungetglyphs(_:_:_:).md)
  Copies a range of glyphs into a user-provided buffer.
- [func CTRunGetPositionsPtr(CTRun) -> UnsafePointer<CGPoint>?](ctrungetpositionsptr(_:).md)
  Returns a direct pointer for the glyph position array stored in the run.
- [func CTRunGetPositions(CTRun, CFRange, UnsafeMutablePointer<CGPoint>)](ctrungetpositions(_:_:_:).md)
  Copies a range of glyph positions into a user-provided buffer.
- [func CTRunGetAdvancesPtr(CTRun) -> UnsafePointer<CGSize>?](ctrungetadvancesptr(_:).md)
  Returns a direct pointer for the glyph advance array stored in the run.
- [func CTRunGetAdvances(CTRun, CFRange, UnsafeMutablePointer<CGSize>)](ctrungetadvances(_:_:_:).md)
  Copies a range of glyph advances into a user-provided buffer.
- [func CTRunGetStringIndicesPtr(CTRun) -> UnsafePointer<CFIndex>?](ctrungetstringindicesptr(_:).md)
  Returns a direct pointer for the string indices stored in the run.
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](ctrungetstringindices(_:_:_:).md)
  Copies a range of string indices into a user-provided buffer.
- [func CTRunGetStringRange(CTRun) -> CFRange](ctrungetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetglyphsptr(_:))*