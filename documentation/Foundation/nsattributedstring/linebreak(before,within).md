# lineBreak(before:within:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func lineBreak(before location: Int, within aRange: NSRange) -> Int
```

```objc
- (NSUInteger) lineBreakBeforeIndex:(NSUInteger) location withinRange:(NSRange) aRange;
```

## Return Value

 Returns the index of the closest character before `index` within `aRange`, that can be placed on a new line when laying out text. Returns `NSNotFound` if no line break is possible before `index`.

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if `index` or any part of `aRange` lies beyond the end of the receiver’s characters.

## Parameters

- `location`: The index in the attributed string.
- `aRange`: The range.

## See Also

### Calculating linguistic units
- [func doubleClick(at: Int) -> NSRange](./doubleclick%28at%29.md)
  Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [func lineBreakByHyphenating(before: Int, within: NSRange) -> Int](./linebreakbyhyphenating%28before,within%29.md)
  Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [func nextWord(from: Int, forward: Bool) -> Int](./nextword%28from,forward%29.md)
  Returns the index of the first character of the word after or before the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/linebreak(before:within:))*