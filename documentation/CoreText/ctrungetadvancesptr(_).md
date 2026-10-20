# CTRunGetAdvancesPtr(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns a direct pointer for the glyph advance array stored in the run.

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
func CTRunGetAdvancesPtr(_ run: CTRun) -> UnsafePointer<CGSize>?
```

```c
extern const CGSize *CTRunGetAdvancesPtr(CTRunRef run);
```

#### Return Value

A valid pointer to an array of `CGSize` structures representing the glyph advance array or `NULL`.

#### Discussion

The advance array will have a length equal to the value returned by [`CTRunGetGlyphCount(_:)`](./ctrungetglyphcount%28_%29.md). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. Should this function return `NULL`, the caller needs allocate its own buffer and call [`CTRunGetAdvances(_:_:_:)`](./ctrungetadvances%28_,_,_%29.md) to fetch the advances. Note that advances alone are not sufficient for correctly positioning glyphs in a line, as a run may have a non-identity matrix or the initial glyph in a line may have a non-zero origin; callers should consider using positions instead.

## Parameters

- `run`: The run whose advances you wish to access.

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
- [func CTRunGetAdvances(CTRun, CFRange, UnsafeMutablePointer<CGSize>)](./ctrungetadvances%28_,_,_%29.md)
  Copies a range of glyph advances into a user-provided buffer.
- [func CTRunGetStringIndicesPtr(CTRun) -> UnsafePointer<CFIndex>?](./ctrungetstringindicesptr%28_%29.md)
  Returns a direct pointer for the string indices stored in the run.
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](./ctrungetstringindices%28_,_,_%29.md)
  Copies a range of string indices into a user-provided buffer.
- [func CTRunGetStringRange(CTRun) -> CFRange](./ctrungetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetadvancesptr(_:))*