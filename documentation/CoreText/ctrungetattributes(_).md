# CTRunGetAttributes(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the attribute dictionary that was used to create the glyph run.

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
func CTRunGetAttributes(_ run: CTRun) -> CFDictionary
```

```c
extern CFDictionaryRefCTRunGetAttributes(CTRunRef run);
```

#### Return Value

A valid [`CFDictionary`](../CoreFoundation/cfdictionary.md) or `NULL` on error or if the run has no attributes.

#### Discussion

The dictionary returned is either the same one that was set as an attribute dictionary on the original attributed string or a dictionary that has been manufactured by the layout engine. Attribute dictionaries can be manufactured in the case of font substitution or if the run is missing critical attributes.

## Parameters

- `run`: The run for which to return attributes.

## See Also

### Getting Glyph Run Data
- [func CTRunGetGlyphCount(CTRun) -> CFIndex](./ctrungetglyphcount%28_%29.md)
  Gets the glyph count for the run.
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
- [func CTRunGetStringRange(CTRun) -> CFRange](./ctrungetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetattributes(_:))*