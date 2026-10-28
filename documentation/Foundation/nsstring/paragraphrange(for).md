# paragraphRange(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSRange) paragraphRangeForRange:(NSRange) range;
```

## Return Value

The range of characters representing the paragraph or paragraphs containing `aRange`, including the paragraph termination characters.

## Discussion

A paragraph is any segment of text delimited by a carriage return (`U+000D`), newline (`U+000A`), or paragraph separator (`U+2029`).

## Parameters

- `range`: A range within the receiver. The range must not exceed the bounds of the receiver.

## See Also

### Determining Line and Paragraph Ranges
- [func getLineStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](./getlinestart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func lineRange(for: NSRange) -> NSRange](./linerange%28for%29.md)
  Returns the range of characters representing the line or lines containing a given range.
- [func getParagraphStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](./getparagraphstart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/paragraphrange(for:))*