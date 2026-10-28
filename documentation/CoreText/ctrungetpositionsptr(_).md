# CTRunGetPositionsPtr(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns a direct pointer for the glyph position array stored in the run.

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
func CTRunGetPositionsPtr(_ run: CTRun) -> UnsafePointer<CGPoint>?
```

```c
extern const CGPoint *CTRunGetPositionsPtr(CTRunRef run);
```

## Return Value

A valid pointer to an array of [`CGPoint`](../CoreFoundation/cgpoint.md) structures, or `NULL`.

## Discussion

The glyph positions in a run are relative to the origin of the line containing the run. The position array will have a length equal to the value returned by [`CTRunGetGlyphCount(_:)`](./ctrungetglyphcount%28_%29.md). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. If this function returns `NULL`, the caller must allocate its own buffer and call [`CTRunGetPositions(_:_:_:)`](./ctrungetpositions%28_,_,_%29.md) to fetch the glyph positions.

## Parameters

- `run`: The run from which to access glyph positions.

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
- [func CTRunGetStringRange(CTRun) -> CFRange](./ctrungetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetpositionsptr(_:))*