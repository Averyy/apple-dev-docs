# lineBreakByHyphenating(before:within:)

**Framework**: Foundation  
**Kind**: method

Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func lineBreakByHyphenating(before location: Int, within aRange: NSRange) -> Int
```

#### Return Value

Returns the index of the closest character before  `index` within `aRange`, that can be placed on a new line by hyphenating. Returns `NSNotFound` if no line break by hyphenation is possible before `index`.

#### Discussion

In other words, during text layout, finds the appropriate line break by hyphenation (the character index at which the hyphen glyph should be inserted) when the character at `index` won’t fit on the same line as the character at the beginning of `aRange`.

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` or any part of `aRange` lies beyond the end of the receiver’s characters.

## Parameters

- `location`: The location in the attributed string.
- `aRange`: The range.

## See Also

- [func doubleClick(at: Int) -> NSRange](nsattributedstring/doubleclick(at:).md)
  Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [func lineBreak(before: Int, within: NSRange) -> Int](nsattributedstring/linebreak(before:within:).md)
  Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [func nextWord(from: Int, forward: Bool) -> Int](nsattributedstring/nextword(from:forward:).md)
  Returns the index of the first character of the word after or before the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/linebreakbyhyphenating(before:within:))*