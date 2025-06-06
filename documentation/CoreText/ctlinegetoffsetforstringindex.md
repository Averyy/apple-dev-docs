# CTLineGetOffsetForStringIndex(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Determines the graphical offset or offsets for a string index.

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
func CTLineGetOffsetForStringIndex(_ line: CTLine, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>?) -> CGFloat
```

#### Return Value

The primary offset along the baseline for `charIndex`, or `0.0` if the line does not support string access.

#### Discussion

This function returns the graphical offset or offsets corresponding to a string index, suitable for movement between adjacent lines or for drawing a custom caret. For moving between adjacent lines, the primary offset can be adjusted for any relative indentation of the two lines; a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) constructed with the adjusted offset for its `x` value and `0.0` for its `y` value is suitable for passing to [`CTLineGetStringIndexForPosition(_:_:)`](ctlinegetstringindexforposition(_:_:).md). For drawing a custom caret, the returned primary offset corresponds to the portion of the caret that represents the visual insertion location for a character whose direction matches the line’s writing direction.

## Parameters

- `line`: The line from which the offset is requested.
- `charIndex`: The string index corresponding to the desired position.
- `secondaryOffset`: On output, the secondary offset along the baseline for  . When a single caret is sufficient for a string index, this value will be the same as the primary offset, which is the return value of this function. May be  .

## See Also

- [func CTLineGetStringIndexForPosition(CTLine, CGPoint) -> CFIndex](ctlinegetstringindexforposition(_:_:).md)
  Performs hit testing.
- [func CTLineEnumerateCaretOffsets(CTLine, (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void)](ctlineenumeratecaretoffsets(_:_:).md)
  Enumerates caret offsets for characters in a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinegetoffsetforstringindex(_:_:_:))*