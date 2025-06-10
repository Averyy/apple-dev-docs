# compare(_:options:range:locale:)

**Framework**: Foundation  
**Kind**: method

Compares the string using the specified options and returns the lexical ordering for the range.

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
func compare(_ string: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToCompare: NSRange, locale: Any?) -> ComparisonResult
```

#### Return Value

Returns an [`ComparisonResult`](comparisonresult.md) value that indicates the lexical ordering of a specified range within the receiver and a given string. [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md) if the substring of the receiver given by `range` precedes `aString` in lexical ordering for the locale given in `dict`, [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md) if the substring of the receiver and `aString` are equivalent in lexical value, and [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md) if the substring of the receiver follows `aString`.

#### Discussion

The `locale` argument affects both equality and ordering algorithms. For example, in some locales, accented characters are ordered immediately after the base; other locales order them after “z”.

## Parameters

- `string`: This value must not be  . If this value is  , the behavior is undefined and may change in future versions of macOS.
- `mask`: See   for details on these options.
- `rangeOfReceiverToCompare`: The range of the receiver over which to perform the comparison. The range must not exceed the bounds of the receiver.
- `locale`: An instance of  . To use the current locale, pass [    ]. For example, if you are comparing strings to present to the end-user, use the current locale. To use the system locale, pass  .

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
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compare(_:options:range:locale:))*