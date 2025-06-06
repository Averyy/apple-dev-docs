# CTLineGetBoundsWithOptions(_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the bounds for a line.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTLineGetBoundsWithOptions(_ line: CTLine, _ options: CTLineBoundsOptions) -> CGRect
```

#### Return Value

The bounds of the line as specified by the type and options, such that the coordinate origin is coincident with the line origin and the rect origin is at the bottom left. If the line is invalid, this function will return [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull).

## Parameters

- `line`: The line for which you calculate the bounds.
- `options`: Desired options or   if none.

## See Also

- [struct CTLineBoundsOptions](ctlineboundsoptions.md)
  Options for getting the bounds of a line of text.
- [func CTRunGetTypographicBounds(CTRun, CFRange, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](ctrungettypographicbounds(_:_:_:_:_:).md)
  Gets the typographic bounds of the run.
- [func CTRunGetImageBounds(CTRun, CGContext?, CFRange) -> CGRect](ctrungetimagebounds(_:_:_:).md)
  Calculates the image bounds for a glyph range.
- [func CTRunGetBaseAdvancesAndOrigins(CTRun, CFRange, UnsafeMutablePointer<CGSize>?, UnsafeMutablePointer<CGPoint>?)](ctrungetbaseadvancesandorigins(_:_:_:_:).md)
  Copies a range of base advances and origins into user-provided buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetboundswithoptions(_:_:))*