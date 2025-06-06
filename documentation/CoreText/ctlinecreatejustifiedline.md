# CTLineCreateJustifiedLine(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a justified line from an existing line.

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
func CTLineCreateJustifiedLine(_ line: CTLine, _ justificationFactor: CGFloat, _ justificationWidth: Double) -> CTLine?
```

#### Return Value

A reference to a justified CTLine object if the call was successful; otherwise, `NULL`.

## Parameters

- `line`: The line from which to create a justified line.
- `justificationFactor`: Full or partial justification. When set to   or greater, full justification is performed. If this parameter is set to less than  , varying degrees of partial justification are performed. If it is set to   or less, no justification is performed.
- `justificationWidth`: The width to which the resultant line is justified. If   is less than the actual width of the line, then negative justification is performed (that is, glyphs are squeezed together).

## See Also

- [func CTLineCreateWithAttributedString(CFAttributedString) -> CTLine](ctlinecreatewithattributedstring(_:).md)
  Creates a single immutable line object from an attributed string.
- [func CTLineCreateTruncatedLine(CTLine, Double, CTLineTruncationType, CTLine?) -> CTLine?](ctlinecreatetruncatedline(_:_:_:_:).md)
  Creates a truncated line from an existing line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinecreatejustifiedline(_:_:_:))*