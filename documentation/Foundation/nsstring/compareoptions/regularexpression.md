# regularExpression

**Framework**: Foundation  
**Kind**: property

The search string is treated as an ICU-compatible regular expression. If set, no other options can apply except [`caseInsensitive`](nsstring/compareoptions/caseinsensitive.md) and [`anchored`](nsstring/compareoptions/anchored.md). You can use this option only with the `rangeOfString:`… methods and [`replacingOccurrences(of:with:options:range:)`](nsstring/replacingoccurrences(of:with:options:range:).md).

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var regularExpression: NSString.CompareOptions { get }
```

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
- [static var diacriticInsensitive: NSString.CompareOptions](nsstring/compareoptions/diacriticinsensitive.md)
  Search ignores diacritic marks.
- [static var widthInsensitive: NSString.CompareOptions](nsstring/compareoptions/widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.
- [static var forcedOrdering: NSString.CompareOptions](nsstring/compareoptions/forcedordering.md)
  Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.
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
- [static var diacriticInsensitive: NSString.CompareOptions](nsstring/compareoptions/diacriticinsensitive.md)
  Search ignores diacritic marks.
- [static var widthInsensitive: NSString.CompareOptions](nsstring/compareoptions/widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/regularexpression)*