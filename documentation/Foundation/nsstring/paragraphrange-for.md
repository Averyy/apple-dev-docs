# paragraphRange(for:)

**Framework**: Foundation  
**Kind**: method

Returns the range of characters representing the paragraph or paragraphs containing a given range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func paragraphRange(for range: NSRange) -> NSRange
```

#### Return Value

The range of characters representing the paragraph or paragraphs containing `aRange`, including the paragraph termination characters.

#### Discussion

A paragraph is any segment of text delimited by a carriage return (`U+000D`), newline (`U+000A`), or paragraph separator (`U+2029`).

## Parameters

- `range`: A range within the receiver. The range must not exceed the bounds of the receiver.

## See Also

- [func getLineStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getlinestart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func lineRange(for: NSRange) -> NSRange](nsstring/linerange(for:).md)
  Returns the range of characters representing the line or lines containing a given range.
- [func getParagraphStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getparagraphstart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/paragraphrange(for:))*