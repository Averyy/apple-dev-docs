# localizedCompare(_:)

**Framework**: Foundation  
**Kind**: method

Compares the string and a given string using a localized comparison.

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
func localizedCompare(_ string: String) -> ComparisonResult
```

#### Return Value

Returns an [`ComparisonResult`](comparisonresult.md) value that indicates the lexical ordering. [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md) the receiver precedes `aString` in lexical ordering, [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md) the receiver and `aString` are equivalent in lexical value, and [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md) if the receiver follows `aString`.

#### Discussion

This method uses the current locale.

> ❗ **Important**:  When working with text that’s presented to the user, use the [`localizedStandardCompare(_:)`](nsstring/localizedstandardcompare(_:).md) method instead.

## Parameters

- `string`: This value must not be  . If this value is  , the behavior is undefined and may change in future versions of macOS.

## See Also

- [func caseInsensitiveCompare(String) -> ComparisonResult](nsstring/caseinsensitivecompare(_:).md)
  Returns the result of invoking [`compare(_:options:)`](nsstring/compare(_:options:).md) with `NSCaseInsensitiveSearch` as the only option.
- [func localizedCaseInsensitiveCompare(String) -> ComparisonResult](nsstring/localizedcaseinsensitivecompare(_:).md)
  Compares the string with a given string using a case-insensitive, localized, comparison.
- [func compare(String) -> ComparisonResult](nsstring/compare(_:).md)
  Returns the result of invoking [`compare(_:options:range:)`](nsstring/compare(_:options:range:).md) with no options and the receiver’s full extent as the range.
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
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizedcompare(_:))*