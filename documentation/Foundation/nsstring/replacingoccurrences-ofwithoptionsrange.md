# replacingOccurrences(of:with:options:range:)

**Framework**: Foundation  
**Kind**: method

Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.

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
func replacingOccurrences(of target: String, with replacement: String, options: NSString.CompareOptions = [], range searchRange: NSRange) -> String
```

#### Return Value

A new string in which all occurrences of `target`, matched using `options`, in `searchRange` of the receiver are replaced by `replacement`.

## Parameters

- `target`: The string to replace.
- `replacement`: The string with which to replace  .
- `options`: A mask of options to use when comparing   with the receiver. Pass   to specify no options.
- `searchRange`: The range in the receiver in which to search for  .

## See Also

- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func replacingOccurrences(of: String, with: String) -> String](nsstring/replacingoccurrences(of:with:).md)
  Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [func replacingCharacters(in: NSRange, with: String) -> String](nsstring/replacingcharacters(in:with:).md)
  Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/replacingoccurrences(of:with:options:range:))*