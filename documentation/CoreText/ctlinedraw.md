# CTLineDraw(_:_:)

**Framework**: Core Text  
**Kind**: func

Draws a complete line.

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
func CTLineDraw(_ line: CTLine, _ context: CGContext)
```

#### Discussion

This is a convenience function because the line could be drawn run-by-run by getting the glyph runs, getting the glyphs out of them, and calling a function such as [`CGContextShowGlyphsAtPositions`](https://developer.apple.com/documentation/coregraphics/1456200-cgcontextshowglyphsatpositions). This call can leave the graphics context in any state and does not flush the context after the draw operation.

## Parameters

- `line`: The line to draw.
- `context`: The context into which the line is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinedraw(_:_:))*