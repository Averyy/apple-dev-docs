# CTRunGetStringRange(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Gets the range of characters that originally spawned the glyphs in the run.

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
func CTRunGetStringRange(_ run: CTRun) -> CFRange
```

```c
extern CFRange CTRunGetStringRange(CTRunRef run);
```

#### Return Value

The range of characters that originally spawned the glyphs, of if `run` is invalid, an empty range.

## Parameters

- `run`: The run for which to access the string range.

## See Also

### Getting Glyph Run Data
- [func CTRunGetGlyphCount(CTRun) -> CFIndex](./ctrungetglyphcount%28_%29.md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](./ctrungetattributes%28_%29.md)
  Returns the attribute dictionary that was used to create the glyph run.
- [func CTRunGetStatus(CTRun) -> CTRunStatus](./ctrungetstatus%28_%29.md)
  Returns the run’s status.
- [func CTRunGetGlyphsPtr(CTRun) -> UnsafePointer<CGGlyph>?](./ctrungetglyphsptr%28_%29.md)
  Returns a direct pointer for the glyph array stored in the run.
- [func CTRunGetGlyphs(CTRun, CFRange, UnsafeMutablePointer<CGGlyph>)](./ctrungetglyphs%28_,_,_%29.md)
  Copies a range of glyphs into a user-provided buffer.
- [func CTRunGetPositionsPtr(CTRun) -> UnsafePointer<CGPoint>?](./ctrungetpositionsptr%28_%29.md)
  Returns a direct pointer for the glyph position array stored in the run.
- [func CTRunGetPositions(CTRun, CFRange, UnsafeMutablePointer<CGPoint>)](./ctrungetpositions%28_,_,_%29.md)
  Copies a range of glyph positions into a user-provided buffer.
- [func CTRunGetAdvancesPtr(CTRun) -> UnsafePointer<CGSize>?](./ctrungetadvancesptr%28_%29.md)
  Returns a direct pointer for the glyph advance array stored in the run.
- [func CTRunGetAdvances(CTRun, CFRange, UnsafeMutablePointer<CGSize>)](./ctrungetadvances%28_,_,_%29.md)
  Copies a range of glyph advances into a user-provided buffer.
- [func CTRunGetStringIndicesPtr(CTRun) -> UnsafePointer<CFIndex>?](./ctrungetstringindicesptr%28_%29.md)
  Returns a direct pointer for the string indices stored in the run.
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](./ctrungetstringindices%28_,_,_%29.md)
  Copies a range of string indices into a user-provided buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetstringrange(_:))*