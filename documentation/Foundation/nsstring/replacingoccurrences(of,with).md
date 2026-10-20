# replacingOccurrences(of:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) stringByReplacingOccurrencesOfString:(NSString *) target withString:(NSString *) replacement;
```

#### Return Value

A new string in which all occurrences of `target` in the receiver are replaced by `replacement`.

#### Discussion

Invokes [`replacingOccurrences(of:with:options:range:)`](./replacingoccurrences%28of,with,options,range%29.md)with `0` options and range of the whole string.

## Parameters

- `target`: The string to replace.
- `replacement`: The string with which to replace `target`.

## See Also

### Related Documentation
- [func replacingPercentEscapes(using: UInt) -> String?](./replacingpercentescapes%28using%29.md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
### Replacing Substrings
- [func replacingOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> String](./replacingoccurrences%28of,with,options,range%29.md)
  Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.
- [func replacingCharacters(in: NSRange, with: String) -> String](./replacingcharacters%28in,with%29.md)
  Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/replacingoccurrences(of:with:))*