# CTRunGetImageBounds(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Calculates the image bounds for a glyph range.

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
func CTRunGetImageBounds(_ run: CTRun, _ context: CGContext?, _ range: CFRange) -> CGRect
```

```c
extern CGRect CTRunGetImageBounds(CTRunRef run, CGContextRef context, CFRange range);
```

#### Return Value

A rectangle that tightly encloses the paths of the run’s glyphs, or, if `run`, `context`, or `range` is invalid, [`CGRectNull`](../CoreGraphics/cgrectnull.md).

## Parameters

- `run`: The run for which to calculate the image bounds.
- `context`: The context for the image bounds being calculated. This is required because the context could have settings in it that would cause changes in the image bounds.
- `range`: The portion of the run to measure. If the length of the range is set to `0`, then the measure operation continues from the start index of the range to the end of the run.

## See Also

### Measuring the Glyph Run
- [func CTLineGetBoundsWithOptions(CTLine, CTLineBoundsOptions) -> CGRect](./ctlinegetboundswithoptions%28_,_%29.md)
  Calculates the bounds for a line.
- [func CTRunGetTypographicBounds(CTRun, CFRange, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](./ctrungettypographicbounds%28_,_,_,_,_%29.md)
  Gets the typographic bounds of the run.
- [func CTRunGetBaseAdvancesAndOrigins(CTRun, CFRange, UnsafeMutablePointer<CGSize>?, UnsafeMutablePointer<CGPoint>?)](./ctrungetbaseadvancesandorigins%28_,_,_,_%29.md)
  Copies a range of base advances and origins into user-provided buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetimagebounds(_:_:_:))*