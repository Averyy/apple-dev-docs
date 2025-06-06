# CTLineEnumerateCaretOffsets(_:_:)

**Framework**: Core Text  
**Kind**: func

Enumerates caret offsets for characters in a line.

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
func CTLineEnumerateCaretOffsets(_ line: CTLine, _ block: @escaping (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void)
```

## Parameters

- `line`: The line to enumerate.
- `block`: The block to invoke once for each logical caret edge in the line, in left-to-right visual order. The block’s   parameter is relative to the line origin. The block’s   parameter specifies logical order.

## See Also

- [func CTLineGetStringIndexForPosition(CTLine, CGPoint) -> CFIndex](ctlinegetstringindexforposition(_:_:).md)
  Performs hit testing.
- [func CTLineGetOffsetForStringIndex(CTLine, CFIndex, UnsafeMutablePointer<CGFloat>?) -> CGFloat](ctlinegetoffsetforstringindex(_:_:_:).md)
  Determines the graphical offset or offsets for a string index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlineenumeratecaretoffsets(_:_:))*