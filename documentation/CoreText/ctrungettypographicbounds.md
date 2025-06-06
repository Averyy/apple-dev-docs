# CTRunGetTypographicBounds(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Gets the typographic bounds of the run.

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
func CTRunGetTypographicBounds(_ run: CTRun, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double
```

#### Return Value

The typographic width of the run, or if `run` or `range` is invalid, `0`.

## Parameters

- `run`: The run for which to calculate the typographic bounds.
- `range`: The portion of the run to measure. If the length of the range is set to  , then the measure operation continues from the range’s start index to the end of the run.
- `ascent`: On output, the ascent of the run. This can be set to   if not needed.
- `descent`: On output, the descent of the run. This can be set to   if not needed.
- `leading`: On output, the leading of the run. This can be set to   if not needed.

## See Also

- [func CTLineGetBoundsWithOptions(CTLine, CTLineBoundsOptions) -> CGRect](ctlinegetboundswithoptions(_:_:).md)
  Calculates the bounds for a line.
- [func CTRunGetImageBounds(CTRun, CGContext?, CFRange) -> CGRect](ctrungetimagebounds(_:_:_:).md)
  Calculates the image bounds for a glyph range.
- [func CTRunGetBaseAdvancesAndOrigins(CTRun, CFRange, UnsafeMutablePointer<CGSize>?, UnsafeMutablePointer<CGPoint>?)](ctrungetbaseadvancesandorigins(_:_:_:_:).md)
  Copies a range of base advances and origins into user-provided buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungettypographicbounds(_:_:_:_:_:))*