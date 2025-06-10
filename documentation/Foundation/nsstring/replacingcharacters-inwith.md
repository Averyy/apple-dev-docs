# replacingCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method

Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.

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
func replacingCharacters(in range: NSRange, with replacement: String) -> String
```

#### Return Value

A new string in which the characters in `range` of the receiver are replaced by `replacement`.

## Parameters

- `range`: A range of characters in the receiver.
- `replacement`: The string with which to replace the characters in  .

## See Also

- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func replacingOccurrences(of: String, with: String) -> String](nsstring/replacingoccurrences(of:with:).md)
  Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [func replacingOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> String](nsstring/replacingoccurrences(of:with:options:range:).md)
  Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/replacingcharacters(in:with:))*