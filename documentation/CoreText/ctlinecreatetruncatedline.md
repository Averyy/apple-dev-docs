# CTLineCreateTruncatedLine(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a truncated line from an existing line.

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
func CTLineCreateTruncatedLine(_ line: CTLine, _ width: Double, _ truncationType: CTLineTruncationType, _ truncationToken: CTLine?) -> CTLine?
```

#### Return Value

A reference to a truncated CTLine object if the call was successful; otherwise, `NULL`.

#### Discussion

The line specified in `truncationToken` should have a width less than the width specified by the `width` parameter. If the width of the line specified in `truncationToken` is greater than `width` and truncation is needed, the function returns `NULL`.

## Parameters

- `line`: The line from which to create a truncated line.
- `width`: The width at which truncation begins. The line is truncated if its width is greater than the width passed in this parameter.
- `truncationType`: The type of truncation to perform if needed. See   for possible values.
- `truncationToken`: This token is added at the point where truncation took place, to indicate that the line was truncated. Usually, the truncation token is the ellipsis character ( ). If this parameter is set to  , then no truncation token is used and the line is simply cut off.

## See Also

- [func CTLineCreateWithAttributedString(CFAttributedString) -> CTLine](ctlinecreatewithattributedstring(_:).md)
  Creates a single immutable line object from an attributed string.
- [func CTLineCreateJustifiedLine(CTLine, CGFloat, Double) -> CTLine?](ctlinecreatejustifiedline(_:_:_:).md)
  Creates a justified line from an existing line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinecreatetruncatedline(_:_:_:_:))*