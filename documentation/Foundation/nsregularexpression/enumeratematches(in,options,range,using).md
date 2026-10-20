# enumerateMatches(in:options:range:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Enumerates the string allowing the Block to handle each regular expression match.

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
func enumerateMatches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange, using block: (NSTextCheckingResult?, NSRegularExpression.MatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateMatchesInString:(NSString *) string options:(NSMatchingOptions) options range:(NSRange) range usingBlock:(void (^)(NSTextCheckingResult *result, NSMatchingFlags flags, BOOL *stop)) block;
```

#### Discussion

This method is the fundamental matching method for regular expressions and is suitable for overriding by subclassers. There are additional convenience methods for returning all the matches as an array, the total number of matches, the first match, and the range of the first match.

By default, the Block iterator method calls the Block precisely once for each match, with a non-`nil` `result` and the appropriate `flags`.  The client may then stop the operation by setting the contents of `stop` to [`true`](../../Swift/true.md). The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the Block.

If the [`reportProgress`](./matchingoptions/reportprogress.md) matching option is specified, the Block will also be called periodically during long-running match operations, with `nil` result and [`progress`](./matchingflags/progress.md) matching flag set in the Block’s `flags` parameter, at which point the client may again stop the operation by setting the contents of stop to [`true`](../../Swift/true.md).

If the [`reportCompletion`](./matchingoptions/reportcompletion.md) matching option is specified, the Block object will be called once after matching is complete, with `nil` result and the [`completed`](./matchingflags/completed.md) matching flag is set in the `flags` passed to the Block, plus any additional relevant [`NSRegularExpression.MatchingFlags`](./matchingflags.md) from among [`hitEnd`](./matchingflags/hitend.md), [`requiredEnd`](./matchingflags/requiredend.md), or [`internalError`](./matchingflags/internalerror.md).

[`progress`](./matchingflags/progress.md) and [`completed`](./matchingflags/completed.md) matching flags have no effect for methods other than this method.

The [`hitEnd`](./matchingflags/hitend.md) matching flag is set in the `flags` passed to the Block if the current match operation reached the end of the search range.  The [`requiredEnd`](./matchingflags/requiredend.md) matching flag is set in the `flags` passed to the Block if the current match depended on the location of the end of the search range.

The [`NSRegularExpression.MatchingFlags`](./matchingflags.md) matching flag is set in the `flags` passed to the block if matching failed due to an internal error (such as an expression requiring exponential memory allocations) without examining the entire search range.

The [`anchored`](./matchingoptions/anchored.md), [`withTransparentBounds`](./matchingoptions/withtransparentbounds.md), and [`withoutAnchoringBounds`](./matchingoptions/withoutanchoringbounds.md) regular expression options, specified in the [`options`](./options-swift.property.md) property specified when the regular expression instance is created, can apply to any match or replace method.

If [`anchored`](./matchingoptions/anchored.md) matching option is specified, matches are limited to those at the start of the search range.

If [`withTransparentBounds`](./matchingoptions/withtransparentbounds.md) matching option is specified, matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc.

If [`withoutAnchoringBounds`](./matchingoptions/withoutanchoringbounds.md) matching option is specified, `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string.

[`withTransparentBounds`](./matchingoptions/withtransparentbounds.md) and [`withoutAnchoringBounds`](./matchingoptions/withoutanchoringbounds.md) matching options have no effect if the search range covers the entire string.

## Parameters

- `string`: The string.
- `options`: The matching options to report. See [`NSRegularExpression.MatchingOptions`](./matchingoptions.md) for the supported values.
- `range`: The range of the string to test.
- `block`: The Block enumerates the matches of the regular expression in the string.

  The block takes three arguments:

  - **result**: An [`NSTextCheckingResult`](../nstextcheckingresult.md) specifying the match. This result gives the overall matched range via its [`range`](../nstextcheckingresult/range.md) property, and the range of each individual capture group via its [`range(at:)`](../nstextcheckingresult/range%28at%29.md) method. The range {`NSNotFound`, 0} is returned if one of the capture groups did not participate in this particular match.
  - **flags**: The current state of the matching progress. See [`NSRegularExpression.MatchingFlags`](./matchingflags.md) for the possible values.
  - **stop**: A reference to a Boolean value. The Block can set the value to [`true`](../../Swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the Block.

  The Block returns void.

## See Also

### Searching Strings Using Regular Expressions
- [func numberOfMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> Int](./numberofmatches%28in,options,range%29.md)
  Returns the number of matches of the regular expression within the specified range of the string.
- [func matches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> [NSTextCheckingResult]](./matches%28in,options,range%29.md)
  Returns an array containing all the matches of the regular expression in the string.
- [func firstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSTextCheckingResult?](./firstmatch%28in,options,range%29.md)
  Returns the first match of the regular expression within the specified range of the string.
- [func rangeOfFirstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSRange](./rangeoffirstmatch%28in,options,range%29.md)
  Returns the range of the first match of the regular expression within the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/enumeratematches(in:options:range:using:))*