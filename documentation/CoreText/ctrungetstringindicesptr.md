# CTRunGetStringIndicesPtr(_:)

**Framework**: Core Text  
**Kind**: func

Returns a direct pointer for the string indices stored in the run.

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
func CTRunGetStringIndicesPtr(_ run: CTRun) -> UnsafePointer<CFIndex>?
```

#### Return Value

A valid pointer to an array of [`CFIndex`](https://developer.apple.com/documentation/CoreFoundation/CFIndex) structures, or `NULL`.

#### Discussion

The indices are the character indices that originally spawned the glyphs that make up the run. They can be used to map the glyphs in the run back to the characters in the backing store. The string indices array will have a length equal to the value returned by [`CTRunGetGlyphCount(_:)`](ctrungetglyphcount(_:).md). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. If this function returns `NULL`, the caller must allocate its own buffer and call [`CTRunGetStringIndices(_:_:_:)`](ctrungetstringindices(_:_:_:).md) to fetch the indices.

## Parameters

- `run`: The run for which to return string indices.

## See Also

- [func CTRunGetGlyphCount(CTRun) -> CFIndex](ctrungetglyphcount(_:).md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](ctrungetattributes(_:).md)
  Returns the attribute dictionary that was used to create the glyph run.
- [func CTRunGetStatus(CTRun) -> CTRunStatus](ctrungetstatus(_:).md)
  Returns the run’s status.
- [func CTRunGetGlyphsPtr(CTRun) -> UnsafePointer<CGGlyph>?](ctrungetglyphsptr(_:).md)
  Returns a direct pointer for the glyph array stored in the run.
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
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](ctrungetstringindices(_:_:_:).md)
  Copies a range of string indices into a user-provided buffer.
- [func CTRunGetStringRange(CTRun) -> CFRange](ctrungetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetstringindicesptr(_:))*