# CTLineGetStringRange(_:)

**Framework**: Core Text  
**Kind**: func

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

#### Return Value

A [`CFRange`](https://developer.apple.com/documentation/CoreFoundation/CFRange) structure that contains the range over the backing store string that spawned the glyphs, or if the function fails for any reason, an empty range.

## Parameters

- `line`: The line from which to obtain the string range.

## See Also

- [func CTLineGetGlyphCount(CTLine) -> CFIndex](ctlinegetglyphcount(_:).md)
  Returns the total glyph count for the line object.
- [func CTLineGetGlyphRuns(CTLine) -> CFArray](ctlinegetglyphruns(_:).md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetPenOffsetForFlush(CTLine, CGFloat, Double) -> Double](ctlinegetpenoffsetforflush(_:_:_:).md)
  Gets the pen offset required to draw flush text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetstringrange(_:))*