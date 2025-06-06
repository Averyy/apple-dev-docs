# CTLineGetGlyphCount(_:)

**Framework**: Core Text  
**Kind**: func

Returns the total glyph count for the line object.

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
func CTLineGetGlyphCount(_ line: CTLine) -> CFIndex
```

#### Return Value

The total glyph count for the line passed in.

#### Discussion

The total glyph count is equal to the sum of all of the glyphs in the glyph runs forming the line.

## Parameters

- `line`: The line whose glyph count is returned.

## See Also

- [func CTLineGetGlyphRuns(CTLine) -> CFArray](ctlinegetglyphruns(_:).md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetStringRange(CTLine) -> CFRange](ctlinegetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the line.
- [func CTLineGetPenOffsetForFlush(CTLine, CGFloat, Double) -> Double](ctlinegetpenoffsetforflush(_:_:_:).md)
  Gets the pen offset required to draw flush text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetglyphcount(_:))*