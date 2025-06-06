# lineBreak(before:within:)

**Framework**: Foundation  
**Kind**: method

Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func lineBreak(before location: Int, within aRange: NSRange) -> Int
```

#### Return Value

 Returns the index of the closest character before `index` within `aRange`, that can be placed on a new line when laying out text. Returns `NSNotFound` if no line break is possible before `index`.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` or any part of `aRange` lies beyond the end of the receiver’s characters.

## Parameters

- `location`: The index in the attributed string.
- `aRange`: The range.

## See Also

- [func doubleClick(at: Int) -> NSRange](nsattributedstring/doubleclick(at:).md)
  Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [func lineBreakByHyphenating(before: Int, within: NSRange) -> Int](nsattributedstring/linebreakbyhyphenating(before:within:).md)
  Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [func nextWord(from: Int, forward: Bool) -> Int](nsattributedstring/nextword(from:forward:).md)
  Returns the index of the first character of the word after or before the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/linebreak(before:within:))*