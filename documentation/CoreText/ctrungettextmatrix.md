# CTRunGetTextMatrix(_:)

**Framework**: Core Text  
**Kind**: func

Returns the text matrix needed to draw this run.

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
func CTRunGetTextMatrix(_ run: CTRun) -> CGAffineTransform
```

#### Return Value

A [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) structure.

#### Discussion

To properly draw the glyphs in a run, the fields `tx` and `ty` of the [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) returned by this function should be set to the current text position.

## Parameters

- `run`: The run object from which to get the text matrix.

## See Also

- [func CTRunDraw(CTRun, CGContext, CFRange)](ctrundraw(_:_:_:).md)
  Draws a complete run or part of one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrungettextmatrix(_:))*