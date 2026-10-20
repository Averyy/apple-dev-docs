# caseInsensitive

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A case-insensitive search.

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
static var caseInsensitive: NSString.CompareOptions { get }
```

```c
NSCaseInsensitiveSearch
```

## See Also

### Constants
- [static var literal: NSString.CompareOptions](./literal.md)
  Exact character-by-character equivalence.
- [static var backwards: NSString.CompareOptions](./backwards.md)
  Search from end of source string.
- [static var anchored: NSString.CompareOptions](./anchored.md)
  Search is limited to start (or end, if `NSBackwardsSearch`) of source string.
- [static var numeric: NSString.CompareOptions](./numeric.md)
  Numbers within strings are compared using numeric value, that is, `Name2.txt` < `Name7.txt` < `Name25.txt`.
- [static var diacriticInsensitive: NSString.CompareOptions](./diacriticinsensitive.md)
  Search ignores diacritic marks.
- [static var widthInsensitive: NSString.CompareOptions](./widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.
- [static var forcedOrdering: NSString.CompareOptions](./forcedordering.md)
  Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.
- [static var regularExpression: NSString.CompareOptions](./regularexpression.md)
  The search string is treated as an ICU-compatible regular expression. If set, no other options can apply except [`caseInsensitive`](./caseinsensitive.md) and [`anchored`](./anchored.md). You can use this option only with the `rangeOfString:`… methods and [`replacingOccurrences(of:with:options:range:)`](../replacingoccurrences%28of,with,options,range%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/caseinsensitive)*