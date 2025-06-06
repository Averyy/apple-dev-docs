# doubleClick(at:)

**Framework**: Foundation  
**Kind**: method

Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func doubleClick(at location: Int) -> NSRange
```

#### Return Value

Returns the range of characters that form a word (or other linguistic unit) surrounding the given index, taking language characteristics into account.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

## Parameters

- `location`: The index in the attributed string.

## See Also

- [func lineBreak(before: Int, within: NSRange) -> Int](nsattributedstring/linebreak(before:within:).md)
  Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [func lineBreakByHyphenating(before: Int, within: NSRange) -> Int](nsattributedstring/linebreakbyhyphenating(before:within:).md)
  Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [func nextWord(from: Int, forward: Bool) -> Int](nsattributedstring/nextword(from:forward:).md)
  Returns the index of the first character of the word after or before the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/doubleclick(at:))*