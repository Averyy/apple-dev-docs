# rangeOfFirstMatch(in:options:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSRange) rangeOfFirstMatchInString:(NSString *) string options:(NSMatchingOptions) options range:(NSRange) range;
```

## Return Value

The range of the first match. Returns `{NSNotFound, 0}` if no match is found.

## Discussion

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
- [func firstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSTextCheckingResult?](./firstmatch%28in,options,range%29.md)
  Returns the first match of the regular expression within the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/rangeoffirstmatch(in:options:range:))*