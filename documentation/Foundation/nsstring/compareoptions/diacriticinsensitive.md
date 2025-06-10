# diacriticInsensitive

**Framework**: Foundation  
**Kind**: property

Search ignores diacritic marks.

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
static var diacriticInsensitive: NSString.CompareOptions { get }
```

#### Discussion

For example, ‘ö’ is equal to ‘o’.

## See Also

- [static var caseInsensitive: NSString.CompareOptions](nsstring/compareoptions/caseinsensitive.md)
  A case-insensitive search.
- [static var literal: NSString.CompareOptions](nsstring/compareoptions/literal.md)
  Exact character-by-character equivalence.
- [static var backwards: NSString.CompareOptions](nsstring/compareoptions/backwards.md)
  Search from end of source string.
- [static var anchored: NSString.CompareOptions](nsstring/compareoptions/anchored.md)
  Search is limited to start (or end, if `NSBackwardsSearch`) of source string.
- [static var numeric: NSString.CompareOptions](nsstring/compareoptions/numeric.md)
  Numbers within strings are compared using numeric value, that is, `Name2.txt` < `Name7.txt` < `Name25.txt`.
- [static var widthInsensitive: NSString.CompareOptions](nsstring/compareoptions/widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.
- [static var forcedOrdering: NSString.CompareOptions](nsstring/compareoptions/forcedordering.md)
  Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.
- [static var regularExpression: NSString.CompareOptions](nsstring/compareoptions/regularexpression.md)
  The search string is treated as an ICU-compatible regular expression. If set, no other options can apply except [`caseInsensitive`](nsstring/compareoptions/caseinsensitive.md) and [`anchored`](nsstring/compareoptions/anchored.md). You can use this option only with the `rangeOfString:`… methods and [`replacingOccurrences(of:with:options:range:)`](nsstring/replacingoccurrences(of:with:options:range:).md).
- [static var caseInsensitive: NSString.CompareOptions](nsstring/compareoptions/caseinsensitive.md)
  A case-insensitive search.
- [static var literal: NSString.CompareOptions](nsstring/compareoptions/literal.md)
  Exact character-by-character equivalence.
- [static var backwards: NSString.CompareOptions](nsstring/compareoptions/backwards.md)
  Search from end of source string.
- [static var anchored: NSString.CompareOptions](nsstring/compareoptions/anchored.md)
  Search is limited to start (or end, if `NSBackwardsSearch`) of source string.
- [static var numeric: NSString.CompareOptions](nsstring/compareoptions/numeric.md)
  Numbers within strings are compared using numeric value, that is, `Name2.txt` < `Name7.txt` < `Name25.txt`.
- [static var widthInsensitive: NSString.CompareOptions](nsstring/compareoptions/widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.
- [static var forcedOrdering: NSString.CompareOptions](nsstring/compareoptions/forcedordering.md)
  Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/diacriticinsensitive)*