# firstMatch(in:options:range:)

**Framework**: Foundation  
**Kind**: method

Returns the first match of the regular expression within the specified range of the string.

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
func firstMatch(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange) -> NSTextCheckingResult?
```

#### Return Value

An [`NSTextCheckingResult`](nstextcheckingresult.md) object. This result gives the overall matched range via its [`range`](nstextcheckingresult/range.md) property, and the range of each individual capture group via its [`range(at:)`](nstextcheckingresult/range(at:).md) method. The range {`NSNotFound`, 0} is returned if one of the capture groups did not participate in this particular match.

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
- [func rangeOfFirstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSRange](nsregularexpression/rangeoffirstmatch(in:options:range:).md)
  Returns the range of the first match of the regular expression within the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/firstmatch(in:options:range:))*