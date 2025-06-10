# getParagraphStart(_:end:contentsEnd:for:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.

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
func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>?, end parEndPtr: UnsafeMutablePointer<Int>?, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>?, for range: NSRange)
```

#### Discussion

A paragraph is any segment of text delimited by a carriage return (`U+000D`), newline (`U+000A`), or paragraph separator (`U+2029`).

If `aRange` is contained with a single paragraph, of course, the returned indexes all belong to that paragraph. Similar to [`getLineStart(_:end:contentsEnd:for:)`](nsstring/getlinestart(_:end:contentsend:for:).md), you can use the results of this method to construct the ranges for paragraphs.

## Parameters

- `startPtr`: Upon return, contains the index of the first character of the paragraph containing the beginning of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `parEndPtr`: Upon return, contains the index of the first character past the terminator of the paragraph containing the end of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `contentsEndPtr`: Upon return, contains the index of the first character of the terminator of the paragraph containing the end of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `range`: A range within the receiver. The value must not exceed the bounds of the receiver.

## See Also

- [func getLineStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getlinestart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func lineRange(for: NSRange) -> NSRange](nsstring/linerange(for:).md)
  Returns the range of characters representing the line or lines containing a given range.
- [func paragraphRange(for: NSRange) -> NSRange](nsstring/paragraphrange(for:).md)
  Returns the range of characters representing the paragraph or paragraphs containing a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getparagraphstart(_:end:contentsend:for:))*