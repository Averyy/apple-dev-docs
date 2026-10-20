# CTLineGetStringRange(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Gets the range of characters that originally spawned the glyphs in the line.

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
func CTLineGetStringRange(_ line: CTLine) -> CFRange
```

```c
extern CFRange CTLineGetStringRange(CTLineRef line);
```

#### Return Value

A [`CFRange`](../CoreFoundation/cfrange.md) structure that contains the range over the backing store string that spawned the glyphs, or if the function fails for any reason, an empty range.

## Parameters

- `line`: The line from which to obtain the string range.

## See Also

### Getting Line Data
- [func CTLineGetGlyphCount(CTLine) -> CFIndex](./ctlinegetglyphcount%28_%29.md)
  Returns the total glyph count for the line object.
- [func CTLineGetGlyphRuns(CTLine) -> CFArray](./ctlinegetglyphruns%28_%29.md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetPenOffsetForFlush(CTLine, CGFloat, Double) -> Double](./ctlinegetpenoffsetforflush%28_,_,_%29.md)
  Gets the pen offset required to draw flush text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetstringrange(_:))*