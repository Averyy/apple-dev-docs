# CTLineGetPenOffsetForFlush(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Gets the pen offset required to draw flush text.

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
func CTLineGetPenOffsetForFlush(_ line: CTLine, _ flushFactor: CGFloat, _ flushWidth: Double) -> Double
```

#### Return Value

The offset from the current pen position for the flush operation.

## Parameters

- `line`: The line from which to obtain a flush position.
- `flushFactor`: Determines the type of flushness. A   of   or less indicates left flush. A   of   or more indicates right flush. Flush factors between   and   indicate varying degrees of center flush, with a value of   being totally center flush.
- `flushWidth`: Specifies the width to which the flushness operation should apply.

## See Also

- [func CTLineGetGlyphCount(CTLine) -> CFIndex](ctlinegetglyphcount(_:).md)
  Returns the total glyph count for the line object.
- [func CTLineGetGlyphRuns(CTLine) -> CFArray](ctlinegetglyphruns(_:).md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetStringRange(CTLine) -> CFRange](ctlinegetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetpenoffsetforflush(_:_:_:))*