# getLineStart(_:end:contentsEnd:for:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the beginning of the first line and the end of the last line touched by the given range.

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
func getLineStart(_ startPtr: UnsafeMutablePointer<Int>?, end lineEndPtr: UnsafeMutablePointer<Int>?, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>?, for range: NSRange)
```

#### Discussion

A line is delimited by any of these characters, the longest possible sequence being preferred to any shorter:

- `U+000A` Unicode Character ‘LINE FEED (LF)’ (`\n`)
- `U+000D` Unicode Character ‘CARRIAGE RETURN (CR)’ (`\r`)
- `U+0085` Unicode Character ‘NEXT LINE (NEL)’
- `U+2028` Unicode Character ‘LINE SEPARATOR’
- `U+2029` Unicode Character ‘PARAGRAPH SEPARATOR’
- `\r\n`, in that order (also known as `CRLF`)

If `aRange` is contained with a single line, of course, the returned indexes all belong to that line. You can use the results of this method to construct ranges for lines by using the start index as the range’s location and the difference between the end index and the start index as the range’s length.

##### Special Considerations

This method detects all invalid ranges (including those with negative lengths). For applications linked against macOS 10.6 and later, this error causes an exception; for applications linked against earlier releases, this error causes a warning, which is displayed just once per application execution.

## Parameters

- `startPtr`: Upon return, contains the index of the first character of the line containing the beginning of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `lineEndPtr`: Upon return, contains the index of the first character past the terminator of the line containing the end of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `contentsEndPtr`: Upon return, contains the index of the first character of the terminator of the line containing the end of  . Pass   if you do not need this value (in which case the work to compute the value isn’t performed).
- `range`: Raises an   if   is invalid.

## See Also

- [func substring(with: NSRange) -> String](nsstring/substring(with:).md)
  Returns a string object containing the characters of the receiver that lie within a given range.
- [func lineRange(for: NSRange) -> NSRange](nsstring/linerange(for:).md)
  Returns the range of characters representing the line or lines containing a given range.
- [func getParagraphStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getparagraphstart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [func paragraphRange(for: NSRange) -> NSRange](nsstring/paragraphrange(for:).md)
  Returns the range of characters representing the paragraph or paragraphs containing a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getlinestart(_:end:contentsend:for:))*