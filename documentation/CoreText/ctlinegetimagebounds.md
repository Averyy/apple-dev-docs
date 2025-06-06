# CTLineGetImageBounds(_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the image bounds for a line.

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
func CTLineGetImageBounds(_ line: CTLine, _ context: CGContext?) -> CGRect
```

#### Return Value

A rectangle that tightly encloses the paths of the line’s glyphs, or, if the line or context is invalid, [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull).

## Parameters

- `line`: The line whose image bounds are calculated.
- `context`: The context for which the image bounds are calculated. This is required because the context could have settings in it that would cause changes in the image bounds.

## See Also

- [func CTLineGetTypographicBounds(CTLine, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](ctlinegettypographicbounds(_:_:_:_:).md)
  Calculates the typographic bounds of a line.
- [func CTLineGetTrailingWhitespaceWidth(CTLine) -> Double](ctlinegettrailingwhitespacewidth(_:).md)
  Returns the trailing whitespace width for a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetimagebounds(_:_:))*