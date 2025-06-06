# rangeOfFirstMatch(in:options:range:)

**Framework**: Foundation  
**Kind**: method

Returns the range of the first match of the regular expression within the specified range of the string.

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
func rangeOfFirstMatch(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange) -> NSRange
```

#### Return Value

The range of the first match. Returns `{NSNotFound, 0}` if no match is found.

#### Discussion

This is a convenience method that calls [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md).

## Parameters

- `string`: The string to search.
- `options`: The matching options to use. See   for possible values.
- `range`: The range of the string to search.

## See Also

- [func numberOfMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> Int](nsregularexpression/numberofmatches(in:options:range:).md)
  Returns the number of matches of the regular expression within the specified range of the string.
- [func enumerateMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange, using: (NSTextCheckingResult?, NSRegularExpression.MatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)](nsregularexpression/enumeratematches(in:options:range:using:).md)
  Enumerates the string allowing the Block to handle each regular expression match.
- [func matches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> [NSTextCheckingResult]](nsregularexpression/matches(in:options:range:).md)
  Returns an array containing all the matches of the regular expression in the string.
- [func firstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSTextCheckingResult?](nsregularexpression/firstmatch(in:options:range:).md)
  Returns the first match of the regular expression within the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/rangeoffirstmatch(in:options:range:))*