# firstMatch(in:options:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSTextCheckingResult *) firstMatchInString:(NSString *) string options:(NSMatchingOptions) options range:(NSRange) range;
```

#### Return Value

An [`NSTextCheckingResult`](../nstextcheckingresult.md) object. This result gives the overall matched range via its [`range`](../nstextcheckingresult/range.md) property, and the range of each individual capture group via its [`range(at:)`](../nstextcheckingresult/range%28at%29.md) method. The range {`NSNotFound`, 0} is returned if one of the capture groups did not participate in this particular match.

#### Discussion

This is a convenience method that calls [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md).

## Parameters

- `string`: The string to search.
- `options`: The matching options to use. See [`NSRegularExpression.MatchingOptions`](./matchingoptions.md) for possible values.
- `range`: The range of the string to search.

## See Also

### Searching Strings Using Regular Expressions
- [func numberOfMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> Int](./numberofmatches%28in,options,range%29.md)
  Returns the number of matches of the regular expression within the specified range of the string.
- [func enumerateMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange, using: (NSTextCheckingResult?, NSRegularExpression.MatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratematches%28in,options,range,using%29.md)
  Enumerates the string allowing the Block to handle each regular expression match.
- [func matches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> [NSTextCheckingResult]](./matches%28in,options,range%29.md)
  Returns an array containing all the matches of the regular expression in the string.
- [func rangeOfFirstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSRange](./rangeoffirstmatch%28in,options,range%29.md)
  Returns the range of the first match of the regular expression within the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/firstmatch(in:options:range:))*