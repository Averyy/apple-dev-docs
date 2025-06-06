# CTRunGetStatus(_:)

**Framework**: Core Text  
**Kind**: func

Returns the run’s status.

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
func CTRunGetStatus(_ run: CTRun) -> CTRunStatus
```

#### Return Value

The run’s status.

#### Discussion

Runs have status that can be used to expedite certain operations. Knowing the direction and ordering of a run’s glyphs can aid in string index analysis, whereas knowing whether the positions reference the identity text matrix can avoid expensive comparisons. This status is provided as a convenience, because this information is not strictly necessary but can be helpful in some circumstances.

## Parameters

- `run`: The run for which to return the status.

## See Also

- [func CTRunGetGlyphCount(CTRun) -> CFIndex](ctrungetglyphcount(_:).md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](ctrungetattributes(_:).md)
  Returns the attribute dictionary that was used to create the glyph run.
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
- [func CTRunGetStringIndicesPtr(CTRun) -> UnsafePointer<CFIndex>?](ctrungetstringindicesptr(_:).md)
  Returns a direct pointer for the string indices stored in the run.
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](ctrungetstringindices(_:_:_:).md)
  Copies a range of string indices into a user-provided buffer.
- [func CTRunGetStringRange(CTRun) -> CFRange](ctrungetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetstatus(_:))*