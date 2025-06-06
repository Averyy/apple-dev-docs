# CTLineGetTypographicBounds(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the typographic bounds of a line.

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
func CTLineGetTypographicBounds(_ line: CTLine, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double
```

#### Return Value

The typographic width of the line. If the line is invalid, this function returns `0`.

## Parameters

- `line`: The line whose typographic bounds are calculated.
- `ascent`: On output, the ascent of the line. This parameter can be set to   if not needed.
- `descent`: On output, the descent of the line. This parameter can be set to   if not needed.
- `leading`: On output, the leading of the line. This parameter can be set to   if not needed.

## See Also

- [func CTLineGetImageBounds(CTLine, CGContext?) -> CGRect](ctlinegetimagebounds(_:_:).md)
  Calculates the image bounds for a line.
- [func CTLineGetTrailingWhitespaceWidth(CTLine) -> Double](ctlinegettrailingwhitespacewidth(_:).md)
  Returns the trailing whitespace width for a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegettypographicbounds(_:_:_:_:))*