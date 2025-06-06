# CFStringGetParagraphBounds(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Given a range of characters in a string, obtains the paragraph bounds—that is, the indexes of the first character and the final characters of the paragraph(s) containing the range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringGetParagraphBounds(_ string: CFString!, _ range: CFRange, _ parBeginIndex: UnsafeMutablePointer<CFIndex>!, _ parEndIndex: UnsafeMutablePointer<CFIndex>!, _ contentsEndIndex: UnsafeMutablePointer<CFIndex>!)
```

#### Discussion

This function is the same as [`CFStringGetLineBounds(_:_:_:_:_:)`](cfstringgetlinebounds(_:_:_:_:_:).md)(), however it only looks for paragraphs (that is, it does not stop at Unicode NextLine or LineSeparator characters).

This function is a convenience function for determining the beginning and ending indexes of one or more paragraph in the given range of a string. It is useful, for example, when each line represents a “record” of some sort; you might search for some substring, but want to extract the record of which the substring is a part.

To determine line separation, the function looks for the standard paragraph-separator characters: carriage returns (CR and CRLF), linefeeds (LF), and Unicode paragraph separators. The three final parameters of the function indirectly return, in order, the index of the first character that starts the line, the index of the first character of the next line (including end-of-line characters), and the index of the last character of the line (excluding end-of-line characters). Pass `NULL` for any of these parameters if you aren’t interested in the result.

To determine the number of characters in the paragraph:

- Subtract `parBeginIndex` from `parEndIndex` to find the number of characters in the paragraph, including the paragraph separators.
- Subtract `parBeginIndex` from `contentsEndIndex` to find the number of characters in the paragraph, excluding the paragraph separators.

## Parameters

- `string`: The string containing the specified range of characters.
- `range`: The range of characters to consider. The specified range must not exceed the length of the string.
- `parBeginIndex`: On return, the index of the first character of the containing paragraph. Pass   if you do not want this result.
- `parEndIndex`: On return, the index of the first character of the paragraph after the specified range. Pass   if you do not want this result.
- `contentsEndIndex`: On return, the index of the last character of the containing paragraph, excluding any paragraph-separator characters. Pass   if you are not interested in this result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetparagraphbounds(_:_:_:_:_:))*