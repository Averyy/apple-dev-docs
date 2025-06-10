# replacingOccurrences(of:with:)

**Framework**: Foundation  
**Kind**: method

Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.

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
func replacingOccurrences(of target: String, with replacement: String) -> String
```

#### Return Value

A new string in which all occurrences of `target` in the receiver are replaced by `replacement`.

#### Discussion

Invokes [`replacingOccurrences(of:with:options:range:)`](nsstring/replacingoccurrences(of:with:options:range:).md)with `0` options and range of the whole string.

## Parameters

- `target`: The string to replace.
- `replacement`: The string with which to replace  .

## See Also

- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func replacingOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> String](nsstring/replacingoccurrences(of:with:options:range:).md)
  Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.
- [func replacingCharacters(in: NSRange, with: String) -> String](nsstring/replacingcharacters(in:with:).md)
  Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/replacingoccurrences(of:with:))*