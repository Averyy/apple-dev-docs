# CTLineGetTrailingWhitespaceWidth(_:)

**Framework**: Core Text  
**Kind**: func

Returns the trailing whitespace width for a line.

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
func CTLineGetTrailingWhitespaceWidth(_ line: CTLine) -> Double
```

#### Return Value

The width of the line’s trailing whitespace. If the line is invalid, this function will always return zero.

#### Discussion

Creating a line for a width can result in a line that is actually longer than the desired width due to trailing whitespace. Although this is typically not an issue due to whitespace being invisible, this function can be used to determine what amount of a line’s width is due to trailing whitespace.

## Parameters

- `line`: The line whose trailing whitespace width is calculated.

## See Also

- [func CTLineGetImageBounds(CTLine, CGContext?) -> CGRect](ctlinegetimagebounds(_:_:).md)
  Calculates the image bounds for a line.
- [func CTLineGetTypographicBounds(CTLine, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](ctlinegettypographicbounds(_:_:_:_:).md)
  Calculates the typographic bounds of a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegettrailingwhitespacewidth(_:))*