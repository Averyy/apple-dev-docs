# CTLineGetPenOffsetForFlush(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern double CTLineGetPenOffsetForFlush(CTLineRef line, CGFloat flushFactor, double flushWidth);
```

## Return Value

The offset from the current pen position for the flush operation.

## Parameters

- `line`: The line from which to obtain a flush position.
- `flushFactor`: Determines the type of flushness. A `flushFactor` of `0` or less indicates left flush. A `flushFactor` of `1.0` or more indicates right flush. Flush factors between `0` and `1.0` indicate varying degrees of center flush, with a value of `0.5` being totally center flush.
- `flushWidth`: Specifies the width to which the flushness operation should apply.

## See Also

### Getting Line Data
- [func CTLineGetGlyphCount(CTLine) -> CFIndex](./ctlinegetglyphcount%28_%29.md)
  Returns the total glyph count for the line object.
- [func CTLineGetGlyphRuns(CTLine) -> CFArray](./ctlinegetglyphruns%28_%29.md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetStringRange(CTLine) -> CFRange](./ctlinegetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetpenoffsetforflush(_:_:_:))*