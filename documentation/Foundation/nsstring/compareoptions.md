# NSString.CompareOptions

**Framework**: Foundation  
**Kind**: struct

These values represent the options available to many of the string classes’ search and comparison methods.

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
struct CompareOptions
```

#### Overview

See [`Searching, Comparing, and Sorting Strings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149) for details on the effects of these options.

## Topics

### Constants
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
- [static var diacriticInsensitive: NSString.CompareOptions](nsstring/compareoptions/diacriticinsensitive.md)
  Search ignores diacritic marks.
- [static var widthInsensitive: NSString.CompareOptions](nsstring/compareoptions/widthinsensitive.md)
  Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.
- [static var forcedOrdering: NSString.CompareOptions](nsstring/compareoptions/forcedordering.md)
  Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.
- [static var regularExpression: NSString.CompareOptions](nsstring/compareoptions/regularexpression.md)
  The search string is treated as an ICU-compatible regular expression. If set, no other options can apply except [`caseInsensitive`](nsstring/compareoptions/caseinsensitive.md) and [`anchored`](nsstring/compareoptions/anchored.md). You can use this option only with the `rangeOfString:`… methods and [`replacingOccurrences(of:with:options:range:)`](nsstring/replacingoccurrences(of:with:options:range:).md).
### Initializers
- [init(rawValue: UInt)](nsstring/compareoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func caseInsensitiveCompare(String) -> ComparisonResult](nsstring/caseinsensitivecompare(_:).md)
  Returns the result of invoking [`compare(_:options:)`](nsstring/compare(_:options:).md) with `NSCaseInsensitiveSearch` as the only option.
- [func localizedCaseInsensitiveCompare(String) -> ComparisonResult](nsstring/localizedcaseinsensitivecompare(_:).md)
  Compares the string with a given string using a case-insensitive, localized, comparison.
- [func compare(String) -> ComparisonResult](nsstring/compare(_:).md)
  Returns the result of invoking [`compare(_:options:range:)`](nsstring/compare(_:options:range:).md) with no options and the receiver’s full extent as the range.
- [func localizedCompare(String) -> ComparisonResult](nsstring/localizedcompare(_:).md)
  Compares the string and a given string using a localized comparison.
- [func compare(String, options: NSString.CompareOptions) -> ComparisonResult](nsstring/compare(_:options:).md)
  Compares the string with the specified string using the given options.
- [func compare(String, options: NSString.CompareOptions, range: NSRange) -> ComparisonResult](nsstring/compare(_:options:range:).md)
  Returns the result of invoking [`compare(_:options:range:locale:)`](nsstring/compare(_:options:range:locale:).md) with a `nil` locale.
- [func compare(String, options: NSString.CompareOptions, range: NSRange, locale: Any?) -> ComparisonResult](nsstring/compare(_:options:range:locale:).md)
  Compares the string using the specified options and returns the lexical ordering for the range.
- [func localizedStandardCompare(String) -> ComparisonResult](nsstring/localizedstandardcompare(_:).md)
  Compares strings as sorted by the Finder.
- [func hasPrefix(String) -> Bool](nsstring/hasprefix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [func hasSuffix(String) -> Bool](nsstring/hassuffix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [func isEqual(to: String) -> Bool](nsstring/isequal(to:).md)
  Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [var hash: Int](nsstring/hash.md)
  An unsigned integer that can be used as a hash table address.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compareoptions)*