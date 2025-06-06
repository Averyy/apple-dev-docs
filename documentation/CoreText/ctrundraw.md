# CTRunDraw(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Draws a complete run or part of one.

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
func CTRunDraw(_ run: CTRun, _ context: CGContext, _ range: CFRange)
```

#### Discussion

This is a convenience call, because the run could be drawn by accessing the glyphs. This call can leave the graphics context in any state and does not flush the context after the draw operation.

## Parameters

- `run`: The run to draw.
- `context`: The context into which to draw the run.
- `range`: The portion of the run to draw. If the length of the range is set to  , then the draw operation continues from the start index of the range to the end of the run.

## See Also

- [func CTRunGetTextMatrix(CTRun) -> CGAffineTransform](ctrungettextmatrix(_:).md)
  Returns the text matrix needed to draw this run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundraw(_:_:_:))*