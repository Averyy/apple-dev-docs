# CTLineGetGlyphRuns(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the array of glyph runs that make up the line object.

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
func CTLineGetGlyphRuns(_ line: CTLine) -> CFArray
```

```c
extern CFArrayRefCTLineGetGlyphRuns(CTLineRef line);
```

#### Return Value

A [`CFArray`](../CoreFoundation/cfarray.md) containing the CTRun objects that make up the line.

## Parameters

- `line`: The line whose glyph run array is returned.

## See Also

### Getting Line Data
- [func CTLineGetGlyphCount(CTLine) -> CFIndex](./ctlinegetglyphcount%28_%29.md)
  Returns the total glyph count for the line object.
- [func CTLineGetStringRange(CTLine) -> CFRange](./ctlinegetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the line.
- [func CTLineGetPenOffsetForFlush(CTLine, CGFloat, Double) -> Double](./ctlinegetpenoffsetforflush%28_,_,_%29.md)
  Gets the pen offset required to draw flush text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetglyphruns(_:))*