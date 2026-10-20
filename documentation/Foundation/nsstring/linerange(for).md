# lineRange(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the range of characters representing the line or lines containing a given range.

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
func lineRange(for range: NSRange) -> NSRange
```

```objc
- (NSRange) lineRangeForRange:(NSRange) range;
```

#### Return Value

The range of characters representing the line or lines containing `aRange`, including the line termination characters. See [`getLineStart(_:end:contentsEnd:for:)`](./getlinestart%28_,end,contentsend,for%29.md) for a discussion of line terminators.

## Parameters

- `range`: A range within the receiver. The value must not exceed the bounds of the receiver.

## See Also

### Related Documentation
- [func substring(with: NSRange) -> String](./substring%28with%29.md)
  Returns a string object containing the characters of the receiver that lie within a given range.
### Determining Line and Paragraph Ranges
- [func getLineStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](./getlinestart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func getParagraphStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](./getparagraphstart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [func paragraphRange(for: NSRange) -> NSRange](./paragraphrange%28for%29.md)
  Returns the range of characters representing the paragraph or paragraphs containing a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/linerange(for:))*