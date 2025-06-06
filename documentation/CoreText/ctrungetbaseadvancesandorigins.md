# CTRunGetBaseAdvancesAndOrigins(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Copies a range of base advances and origins into user-provided buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTRunGetBaseAdvancesAndOrigins(_ runRef: CTRun, _ range: CFRange, _ advancesBuffer: UnsafeMutablePointer<CGSize>?, _ originsBuffer: UnsafeMutablePointer<CGPoint>?)
```

#### Discussion

A run’s base advances and origins determine the positions of its glyphs but require additional processing before being used for drawing.

Similar to the advances returned by [`CTRunGetAdvances(_:_:_:)`](ctrungetadvances(_:_:_:).md), base advances are the displacement from the origin of a glyph to the origin of the next glyph, except base advances do not include any positioning the font layout tables may have done relative to another glyph (such as a mark relative to its base).

The displacement of the current glyph’s origin from the starting position determines the glyph’s actual position, and the displacement of the current glyph’s base advance from the starting position determines the position of the next glyph.

## Parameters

- `runRef`: The run that contains the base advances and origins you wish to copy.
- `range`: The range of values to be copied. If the length of the range is set to  , the copy operation continues from the range’s start index to the end of the run.
- `advancesBuffer`: The buffer to which the base advances will be copied, or  . If not  , the buffer must allow for at least as many elements as specified by the range’s length.
- `originsBuffer`: The buffer to which the origins will be copied, or  . If not  , the buffer must allow for at least as many elements as specified by the range’s length.

## See Also

- [func CTRunGetAdvances(CTRun, CFRange, UnsafeMutablePointer<CGSize>)](ctrungetadvances(_:_:_:).md)
  Copies a range of glyph advances into a user-provided buffer.
- [func CTLineGetBoundsWithOptions(CTLine, CTLineBoundsOptions) -> CGRect](ctlinegetboundswithoptions(_:_:).md)
  Calculates the bounds for a line.
- [func CTRunGetTypographicBounds(CTRun, CFRange, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](ctrungettypographicbounds(_:_:_:_:_:).md)
  Gets the typographic bounds of the run.
- [func CTRunGetImageBounds(CTRun, CGContext?, CFRange) -> CGRect](ctrungetimagebounds(_:_:_:).md)
  Calculates the image bounds for a glyph range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungetbaseadvancesandorigins(_:_:_:_:))*