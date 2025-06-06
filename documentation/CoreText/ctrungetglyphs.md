# CTRunGetGlyphs(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Copies a range of glyphs into a user-provided buffer.

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
func CTRunGetGlyphs(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>)
```

## Parameters

- `run`: The run from which to copy glyphs.
- `range`: The range of glyphs to copy. If the length of the range is set to  , then the copy operation continues from the range’s start index to the end of the run.
- `buffer`: The buffer the glyphs are copied to. The buffer must be allocated to at least the value specified by the range’s length.

## See Also

- [func CTRunGetGlyphCount(CTRun) -> CFIndex](ctrungetglyphcount(_:).md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](ctrungetattributes(_:).md)
  Returns the attribute dictionary that was used to create the glyph run.
- [func CTRunGetStatus(CTRun) -> CTRunStatus](ctrungetstatus(_:).md)
  Returns the run’s status.
- [func CTRunGetGlyphsPtr(CTRun) -> UnsafePointer<CGGlyph>?](ctrungetglyphsptr(_:).md)
  Returns a direct pointer for the glyph array stored in the run.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetglyphs(_:_:_:))*